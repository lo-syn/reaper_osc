from pythonosc.udp_client import SimpleUDPClient

def reaper_play(client):
    client.send_message("/action", 1007)