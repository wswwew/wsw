import socket,sys

def communicate(cli_sock):
    while True:
        data = input('> ') + '\r\n'
        c.send(data.encode())  # 将str转为bytes类型
        if data.strip() == 'quit':
            break
        print(c.recv(1024).decode())

if __name__ == '__main__':
    host=sys.argv[1]
    port=int(sys.argv[2])
    addr=(host,port)  #客户端要连接的服务器地址
    c = socket.socket()
    c.connect(addr)
    communicate(c)
    c.close()