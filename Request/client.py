
import pika, uuid

def on_replay_message_received(ch, method, properties, body):
    print(f'reply recieved: {body}')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()
exc_name = 'pubsub'

reply_queue = channel.queue_declare(queue='', exclusive=True)
channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_replay_message_received)
channel.queue_declare(queue='request-name')
message = 'Mensaje a entregar.'

cor_id = str(uuid.uuid4())
channel.basic_publish(
    exchange='',
    routing_key='request-queue', 
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ),
    body=message)
print('Mensaje enviado.')
channel.start_consuming()
