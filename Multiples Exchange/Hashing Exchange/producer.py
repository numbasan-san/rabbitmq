
import pika

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare('simple_hashing', "x-consistent-hash")

routing_key='Hashqwertyuikmnbvcd789654 me!'
message = 'Multi message.'
channel.basic_publish(
    exchange='simple_hashing', 
    routing_key=routing_key, 
    body=message
)
print('Mensaje enviado.')
conn.close()
