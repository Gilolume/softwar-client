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

def connectToReqServer(port):
    context = zmq.Context()
    print "Connecting to server..."
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:%s" % port)
    return socket

def putRequest(socket, request):
    print "Sending request ", request,"..."
    socket.send (request)
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"