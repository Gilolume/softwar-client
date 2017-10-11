import command

def play(socket_req):
    command.command_identify(socket_req, "#0x01")
    command.command_forward(socket_req)
    command.command_backward(socket_req)
    command.command_leftfwd(socket_req)
    command.command_rightfwd(socket_req)
    command.command_right(socket_req)
    command.command_left(socket_req)
    command.command_looking(socket_req)
    command.command_gather(socket_req)
    command.command_watch(socket_req)
    command.command_attack(socket_req)
    command.command_selfid(socket_req)
    command.command_selfstats(socket_req)
    command.command_inspect(socket_req, "#0x02")
    command.command_next(socket_req)
    command.command_jump(socket_req)
