
import pika, time
from pika.exchange_type import ExchangeType

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange='header_exchange', exchange_type=ExchangeType.headers)

message = 'Multi message.'
channel.basic_publish(
    exchange='header_exchange', 
    routing_key='', 
    body=message,
    properties=pika.BasicProperties(
    headers={'name': 'brian'}
    )
)
print('Mensaje enviado.')
conn.close()
