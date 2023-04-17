
import pika, time
from pika.exchange_type import ExchangeType

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange='first_exchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='second_exchange', exchange_type=ExchangeType.fanout)

channel.exchange_bind('second_exchange', 'first_exchange')

message = 'Multi message.'
channel.basic_publish(exchange='first_exchange', routing_key='', body=message)
print('Mensaje enviado.')
conn.close()
