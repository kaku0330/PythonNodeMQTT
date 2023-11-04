const mqtt = require('mqtt')
const opt = {
	clientId:"testnode",
	port:1883,
	username:"ubuntu",
	password:"123456"
}

const client = mqtt.connect("mqtt://192.168.0.7", opt)


client.on("connect",function(){
	console.log("connect work")
	client.subscribe("hello")
})
client.on('message', function(topic, payload){
  console.log('Received Message:', topic, payload.toString())
})
