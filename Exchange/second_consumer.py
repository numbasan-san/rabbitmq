
import pika, time, random
from pika.exchange_type import *

consumer_name = 'second_consumer'
exc_name = 'pubsub'

def op_message_recive(ch, method, properties, body):
    print(f'{consumer_name}: recibibe {body}.')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange = exc_name, exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange=exc_name, queue=queue.method.queue)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue=queue.method.queue, auto_ack=True,on_message_callback=op_message_recive)

print('consumeindo... ')
channel.start_consuming()
