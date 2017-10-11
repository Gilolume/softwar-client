import myZmqFunc

def command_identify(socket_req, param):
    myZmqFunc.putRequest(socket_req, "identify|" + param)

def command_forward(socket_req):
    myZmqFunc.putRequest(socket_req, "forward|null")

def command_backward(socket_req):
    myZmqFunc.putRequest(socket_req, "backward|null")

def command_leftfwd(socket_req):
    myZmqFunc.putRequest(socket_req, "leftfwd|null")

def command_rightfwd(socket_req):
    myZmqFunc.putRequest(socket_req, "rightfwd|null")

def command_right(socket_req):
    myZmqFunc.putRequest(socket_req, "right|null")

def command_left(socket_req):
    myZmqFunc.putRequest(socket_req, "left|null")

def command_looking(socket_req):
    myZmqFunc.putRequest(socket_req, "looking|null")

def command_gather(socket_req):
    myZmqFunc.putRequest(socket_req, "gather|null")

def command_watch(socket_req):
    myZmqFunc.putRequest(socket_req, "watch|null")

def command_attack(socket_req):
    myZmqFunc.putRequest(socket_req, "attack|null")

def command_selfid(socket_req):
    myZmqFunc.putRequest(socket_req, "selfid|null")

def command_selfstats(socket_req):
    myZmqFunc.putRequest(socket_req, "selfstats|null")

def command_inspect(socket_req, param):
    myZmqFunc.putRequest(socket_req, "inspect|" + param)

def command_next(socket_req):
    myZmqFunc.putRequest(socket_req, "next|null")

def command_jump(socket_req):
    myZmqFunc.putRequest(socket_req, "jump|null")