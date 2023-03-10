import network
import time

ssid = 'DNA-WLAN-2G-8008' # home: DNA-WLAN-2G-8008 - School: KME662
password = '60846109170' # home: 60846109170 - School: SmartIot


def connectWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    wlan.config(pm = 0xa11140)
    max_wait = 10
    
    # Wait for connect or fail
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
        status = 0
    else:
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )

