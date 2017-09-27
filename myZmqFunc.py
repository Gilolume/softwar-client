import random
import sys
import time
from multiprocessing import Process

import zmq

def connectToPubServer(port):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://localhost:%s" % port)
    return socket

def getNotification(socket):
    socket.setsockopt(zmq.SUBSCRIBE, "")
    response = socket.recv()
    return response