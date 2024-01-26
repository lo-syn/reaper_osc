from pythonosc.udp_client import SimpleUDPClient
import socket
import time
import subprocess

def reaper_start(exe_dir, hide_gui: bool):
    try:
        if hide_gui == True:
            process = subprocess.Popen(exe_dir, stdout=subprocess.DEVNULL, creationflags=0x08000000)
        else:
            process = subprocess.Popen(exe_dir, stdout=subprocess.DEVNULL)
    except subprocess.SubprocessError as error:
        print(error)

    return process

def reaper_client_setup(port):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    client = SimpleUDPClient(ip_address, port)  # Create client
    time.sleep(1) # Required to let UDP Client initialise

    return client

def reaper_play(client):
    client.send_message("/action", 1007)

def reaper_stop(client):
    client.send_message("/action", 1016)

def reaper_record(client):
    client.send_message("/action", 1013)