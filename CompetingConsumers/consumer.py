import pika
import time
import random


def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1,6)
    print(f'Received {body}. It will take {processing_time} seconds.')
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('finished processing the message')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

# only one message at a time
channel.basic_qos(prefetch_count=1)

# no auto acknowledge, drop auto_ack=True
channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print('started consuming')

channel.start_consuming()