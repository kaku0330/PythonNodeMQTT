import paho.mqtt.client as mqtt


def on_connect(client, userdata,flags,rc):
    client.subscribe("johnny/test",True)
def on_message(client,userdata,msg):
    print(msg.payload.decode("utf-8"))



client = mqtt.Client("testa")

client.on_connect = on_connect

client.on_message = on_message

client.username_pw_set(username="root",password="123456") #123456

client.connect("192.168.0.18",1883)

client.on_connect = on_connect

client.loop_forever()