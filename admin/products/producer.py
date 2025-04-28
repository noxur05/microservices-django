import pika

params = pika.URLParameters('amqps://scxgvzem:18t43MB889WMv3N2Ln61j4virXspjWXM@porpoise.rmq.cloudamqp.com/scxgvzem')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')