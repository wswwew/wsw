import socket

host='127.0.0.1'
port=12345
addr=(host,port)
cs=socket.socket(type=socket.SOCK_DGRAM)

while True:
    date=input('> ')+'\r\n'
    if date.strip() == 'quit':
        break
    cs.sendto(date.encode(),addr)
    #print(cs.recvfrom(1024))
    print(cs.recvfrom(1024)[0].decode())

cs.close()