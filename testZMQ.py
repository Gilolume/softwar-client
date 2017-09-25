import zmq
import time
import sys
import random
from  multiprocessing import Process


def zmqTry():
    print "Connecting to hello world server ...\n"
    context = zmq.Context()

    requester = context.socket(zmq.REQ)
    requester.connect("tcp://localhost:5555")

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5556")

    print "Sending Hello ", "\n"
    requester.send("Hello")
    reqBuffer = requester.recv()
    print "[REP-REQ] Received ", "\n", reqBuffer

    subscriber.setsockopt(zmq.SUBSCRIBE, "")
    subBuffer = subscriber.recv()
    print "[PUB-SUB] Received ", "\n", subBuffer
    
    requester.close()
    subscriber.close()
    context.destroy()

def test2():
    # Prepare our context and sockets
    context = zmq.Context()

    # Connect to task ventilator
    requester = context.socket(zmq.REQ)
    requester.connect("tcp://localhost:5555")

    # Connect to weather server
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5556")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"10001")

    # Initialize poll set
    poller = zmq.Poller()
    poller.register(requester, zmq.POLLIN)
    poller.register(subscriber, zmq.POLLIN)

    # Process messages from both sockets
    should_continue = True
    while should_continue:
        #try:
        #    socks = dict(poller.poll())
        #    print socks
        #except KeyboardInterrupt:
        #    break
        #
        #if requester in socks:
        message = requester.send("Hello")
            # process task

        #if subscriber in socks:
        message = subscriber.recv()
        # process weather update
        print message
        requester.close()
        subscriber.close()
        context.destroy()
        should_continue = False
