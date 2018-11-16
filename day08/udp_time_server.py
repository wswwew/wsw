import socket
import time

host=''
port =12345
addr = (host,port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    data,cli_addr = s.recvfrom(1024) #接收的是一个两元素元组,cli_addr取的是后面的值,等于客户端的ip地址和端口
    data=data.decode().strip()
    if data == 'quit':
        break
    print(data)
    data = '[%s] %s\r\n' % (time.strftime('%H:%M:%S',data.strip()))
    s.sendto(data.encode(),cli_addr)

s.close()