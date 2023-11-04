import paho.mqtt.client as mqtt
from paho.mqtt import publish
from paho.mqtt.publish import single
import time,random
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json

class Aescbc:

	def __init__(self,key,iv,msg,lockmsg):
		self.key = key
		self.iv = iv
		self.msg = json.dumps(msg)
		self.lockmsg = lockmsg

	def aes_encrypt(self):
		

		lenmsg = 16-len(self.msg)%16
		for x in range(0,lenmsg):
			self.msg=str(self.msg)+"*"
		cipher = AES.new(self.key.encode("utf-8"),AES.MODE_CBC,self.iv.encode("utf-8"))
		encrypt_aes = cipher.encrypt(self.msg.encode("utf-8"))

		return encrypt_aes.hex()

	def aes_decrypt(self):

		cipher = AES.new(self.key.encode("utf-8"),AES.MODE_CBC,self.iv.encode("utf-8"))
		decrypt_aes = cipher.decrypt(unhexlify(self.lockmsg)).decode("utf-8")

		# plain_text = unpad(decrypt_text.decode("utf-8"),AES.block_size)
		return decrypt_aes



if __name__ == '__main__':
	iv = "pEmqKNVIkH5FY3ev"
	key = "3e83b13d99bf0de6c6bde5ac5ca4ae68"
	#msg = {"ID" : random.randint(1000, 9999), "Name" : "johnny" , "Age" : 777, "Address" : "Taipei", "Nick name" : "BOB"}
	lockmsg = ""
	lastmsg = ""

	#client = mqtt.Client()

	def on_publish(client,userdata,result):
		print("data published \n")
		pass
	#lient.connect("192.168.0.7",1883)

	#client.publish("hello",lockmsg)
	# while True:
	msg = {"ID" : random.randint(1000, 9999), "Name" : "johnny" , "Age" : 777, "Address" : "Taipei", "Nick name" : "BOB"}
	caesar = Aescbc(key,iv,msg,lockmsg)
	lockmsg = caesar.aes_encrypt()
	client = mqtt.Client("testpub",True)
	client.on_publish = on_publish
	client.username_pw_set("johnny","123456")
	client.connect("192.168.0.7",1883)
	client.publish("johnny/test/A", lockmsg, qos=1,retain=False)
	#client.publish("johnny/test/A", "last message--------------", qos=1,retain=True)
	# client.publish("johnny/test/A", "", qos=1,retain=True) #retain=False
	#client.loop_start()
	#client.loop_stop()
	print(lockmsg)
		# time.sleep(1)
	    
	#time.sleep(1)
	# mosquitto_pub -d -h 192.168.0.7 -p 1883 -u johnny -P 123456 -t johnny/test/A -m "1234" -q 2