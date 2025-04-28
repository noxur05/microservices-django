import pika

params = pika.URLParameters('amqps://scxgvzem:18t43MB889WMv3N2Ln61j4virXspjWXM@porpoise.rmq.cloudamqp.com/scxgvzem')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved Admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()