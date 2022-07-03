import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# each exchange its dedicated queue
#channel.queue_declare(queue='letterbox')

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = 'I want to broadcast this.'

channel.basic_publish(exchange='pubsub', routing_key='letterbox', body=message)

print(f'sent message {message}')

connection.close()



