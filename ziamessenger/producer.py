#!/usr/bin/python

from stompest.config import StompConfig
from stompest.sync import Stomp

CONFIG = StompConfig('tcp://localhost:61613')
QUEUE = '/queue/test'

if __name__ == '__main__':
    client = Stomp(CONFIG)
    client.connect()
    client.send(QUEUE, 'Hello'.encode())
    client.send(QUEUE, 'YAYYYYYY'.encode())
    client.disconnect()
