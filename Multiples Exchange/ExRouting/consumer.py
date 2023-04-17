
import pika
from pika.exchange_type import *

def op_message_recive(ch, method, properties, body):
    print(f'recibibo {body}.')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange = 'second_exchange', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='letterbox', exclusive=True)

channel.queue_bind('letterbox', 'second_exchange')

channel.basic_consume(queue=queue.method.queue, auto_ack=True,on_message_callback=op_message_recive)

print('consumeindo... ')
channel.start_consuming()
