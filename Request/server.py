
import pika

def on_replay_message_received(ch, method, properties, body):
    print(f'reply recieved: {properties.correlation_id}')
    ch.basic_publish('', routing_key=properties.reply_to, body=f'Contestación al mensaje de antes a {properties.correlation_id}')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.queue_declare(queue='request-queue')
channel.basic_consume(queue='request-queue', auto_ack=True, on_message_callback=on_replay_message_received)
print('Iniciaclizando servidor.')
channel.start_consuming()
