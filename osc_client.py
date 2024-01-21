from pythonosc.udp_client import SimpleUDPClient
import time
import socket
import numpy as np
import math

hostname = socket.gethostname()
#ip_address = socket.gethostbyname(hostname)
ip_address = '192.168.7.2 '

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

port = 8000

client = SimpleUDPClient(ip_address, port)  # Create client
 
print(f"OSC Client Created. Sending messages")

PLAY="t/play"
STOP="t/stop"

time.sleep(1) # Required to let UDP Client initialise

client.send_message(PLAY, None)

db_step = 1/120

db = 1 - (24*db_step)


for i in range(3):
    message = "/track/1/volume " + str(i)
    print(message)
    client.send_message("/track/1/volume", db)   # Send float message
    #client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
 
    time.sleep(3)


limiter_step = 1/72
zero_db = 1-(12*limiter_step)-(12*limiter_step)

client.send_message("n/track/1/fx/1/fxparam/1/value", zero_db)

time.sleep(4)

client.send_message(STOP, None) 