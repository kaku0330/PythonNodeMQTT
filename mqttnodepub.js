const mqtt = require('mqtt')
const opt = {
	clientId:"testnode",
	port:1883,
	username:"johnny",
	password:"123456"
}

const client = mqtt.connect("mqtt://192.168.0.7", opt)
var option={
	retain:true,
	qos:1
}

client.on("connect",function(){
	console.log("connect work")
	client.publish("johnny/test/A","testnode",option)
})



