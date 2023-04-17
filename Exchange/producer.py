
import pika, time, random
from pika.exchange_type import *

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()
exc_name = 'pubsub'

channel.exchange_declare(exchange = exc_name, exchange_type=ExchangeType.fanout)

message = f'''Hello, I want to broadcast this message.'''

channel.basic_publish(exchange=exc_name, routing_key='', body=message)

print(f'{message}')

channel.close()
