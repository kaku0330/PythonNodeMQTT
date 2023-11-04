import paho.mqtt.client as mqtt
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json
import time,random
from send import *

class Aescbc:

	def __init__(self,key,iv,msg,lockmsg):
		self.key = key
		self.iv = iv
		self.msg = msg
		self.lockmsg = lockmsg

	def aes_encrypt(self):
		

		lenmsg = 16-len(self.msg)%16
		for x in range(0,lenmsg):
			self.msg=self.msg+"*"
		cipher = AES.new(self.key.encode("utf-8"),AES.MODE_CBC,self.iv.encode("utf-8"))
		encrypt_aes = cipher.encrypt(self.msg.encode("utf-8"))

		return encrypt_aes.hex()

	def aes_decrypt(self):

		cipher = AES.new(self.key.encode("utf-8"),AES.MODE_CBC,self.iv.encode("utf-8"))
		decrypt_aes = cipher.decrypt(unhexlify(self.lockmsg)).decode("utf-8")

		# plain_text = unpad(decrypt_text.decode("utf-8"),AES.block_size)
		return decrypt_aes

if __name__ == '__main__':


	# iv = "pEmqKNVIkH5FY3ev"
	# key = "3e83b13d99bf0de6c6bde5ac5ca4ae68"
	# msg = "apple_apple_apple_apple_apple_apple_apple_" 
	# lockmsg = ""
	# lastmsg = ""

	rabbitsend = Rabbitmqsend()
	def on_connect(client, userdata,flags,rc):
		#print("connected with result code "+ str(rc))
		client.subscribe("johnny/test/A",True)

	def on_message(client,userdata,msg):
		#aescbc = Aescbc(key,iv,msg,msg.payload.decode("utf-8"))
		#lastmsg = aescbc.aes_decrypt()
		#print(msg.topic+" "+lastmsg.split("*")[0])
		rabbitsend.publishrabbit(msg.payload.decode("utf-8"))
		#print(msg.payload.decode("utf-8"))
		#client.publish("johnny/test/A", "", qos=1,retain=True)
		#client.disconnect()



	client = mqtt.Client("testa")

	client.on_connect = on_connect

	client.on_message = on_message

	client.username_pw_set(username="root",password="123456") #123456

	client.connect("192.168.0.7",1883)

	client.on_connect = on_connect

	client.loop_forever()

	#mosquitto_sub -d -h 192.168.0.7 -p 1883 -u root -P 123456 -t johnny/test/A -q 2