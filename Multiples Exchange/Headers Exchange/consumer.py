
import pika
from pika.exchange_type import *

def op_message_recive(ch, method, properties, body):
    print(f'recibibo {body}.')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange = 'header_exchange', exchange_type=ExchangeType.headers)

queue = channel.queue_declare(queue='letterbox')

bind_args = {
    'x-match': 'any',
    'name': 'brian',
    'age': '53'
}

channel.queue_bind('letterbox', 'header_exchange', arguments=bind_args)

channel.basic_consume(queue=queue.method.queue, auto_ack=True,on_message_callback=op_message_recive)

print('consumeindo... ')
channel.start_consuming()
