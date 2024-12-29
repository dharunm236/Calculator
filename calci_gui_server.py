import socket
import operator

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ops={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.floordiv,"&":operator.and_,"|":operator.or_,"~":operator.not_}
server.bind(('localhost',12345))

while 1:
    msg,addr=server.recvfrom(2048)
    msg=msg.decode()
    if(msg=="OFF"):
        break
    try:
        result = str(eval(msg))
    except:
        result="ERROR"
    msg=result
    server.sendto(msg.encode(),addr)
    print("MSG SENT SUCCESS")
