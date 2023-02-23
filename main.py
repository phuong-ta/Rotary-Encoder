from rotary import Rotary
from WifiConnection import connectWifi
from umqtt.simple import MQTTClient
from machine import Pin, Timer
#
connectWifi() # ip address

rotary = Rotary(11,10,12)
val = 0
c = MQTTClient(client_id=b"bigles",
    server=b"bec3bbc6c9c44b4fae7e5a42781338c5.s2.eu.hivemq.cloud", 
    port=8883, 
    user=b"tester", 
    password=b"12345678", 
    keepalive=3600,
    ssl=True,
    ssl_params={'server_hostname':'bec3bbc6c9c44b4fae7e5a42781338c5.s2.eu.hivemq.cloud'} 
    )
c.connect()

def publishMsg(msg):
    #mes = b"{}".format(msg)
    c.publish(b"my/test/topic", b"{}".format(msg))
    
def main(change):
    tim = Timer()
    global val
    if change == Rotary.ROT_CW:
        val = val + 1
        print(val)
        tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t:publishMsg("right"))
    elif change == Rotary.ROT_CCW:
        val = val - 1
        print(val)
        tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t:publishMsg("left"))
    elif change == Rotary.SW_PRESS:
        print('PRESS')
        tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t:publishMsg("down"))
    elif change == Rotary.SW_RELEASE:
        print('RELEASE')

rotary.add_handler(main)