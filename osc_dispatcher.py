from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
import socket

dispatcher = Dispatcher()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

port = 8000

server = BlockingOSCUDPServer((ip_address, 8000), dispatcher)
client = SimpleUDPClient(ip_address, 8000)

# Send message and receive exactly one message (blocking)
client.send_message("/track/3/volume", 0.5)
print(server.handle_request())

