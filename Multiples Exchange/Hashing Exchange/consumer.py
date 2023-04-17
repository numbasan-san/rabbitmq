
import pika

def op_message1_recived(ch, method, properties, body):
    print(f'Cola 1 recibibo {body}.')
def op_message2_recived(ch, method, properties, body):
    print(f'Cola 2 recibibo {body}.')

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare('simple_hashing', "x-consistent-hash")

channel.queue_declare(queue='letterbox1')
channel.queue_bind('letterbox1', 'simple_hashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True, on_message_callback=op_message1_recived)

channel.queue_declare(queue='letterbox2')
channel.queue_bind('letterbox2', 'simple_hashing', routing_key='2')
channel.basic_consume(queue='letterbox2', auto_ack=True, on_message_callback=op_message2_recived)

print('consumeindo... ')
channel.start_consuming()
