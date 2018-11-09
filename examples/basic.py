import microgear.client as microgear
import time
import logging

appid = <Unbalance>
gearkey = <hGCHSVuHP92G1Xk>
gearsecret =  <IdLciZCa6M4SHjmc7Edt2NE64>

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    logging.info("Now I am connected with netpie")

def subscription(topic,message):
    logging.info(topic+" "+message)

def disconnect():
    logging.debug("disconnect is work")

microgear.setalias("doraemon")
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/mails")
microgear.connect(False)

while True:
	if(microgear.connected):
		microgear.chat("doraemon","Hello world."+str(int(time.time())))
	time.sleep(3)
