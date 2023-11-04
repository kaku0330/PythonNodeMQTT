import pika

#passwd = pika.PlainCredentials("admin","123456")
# connection = pika.BlockingConnection(
# 	pika.ConnectionParameters("192.168.0.6",5672,"/",passwd))
# channel = connection.channel()

# channel.basic_publish(exchange="",routing_key="test",body="12345")
# print("[x] sent '12345'")
# connection.close()


class Rabbitmqsend:

	
	def publishrabbit(self,msg):
		connection = pika.BlockingConnection(
			pika.ConnectionParameters("192.168.0.6",5672,"/",pika.PlainCredentials("admin","123456")))
		channel = connection.channel()
		channel.basic_publish(exchange="",routing_key="test",body=msg)
		#print("[x] sent " + msg)
		connection.close()