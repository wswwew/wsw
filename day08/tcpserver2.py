import socket,time

host = ''
port = 12345
addr = (host,port)
s = socket.socket()

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cli_sock,cli_addr =s.accept() #接收的是一个两元素元组,cli_addr取的是后面的值,等于客户端的ip地址和端口
    except KeyboardInterrupt:
        break
    print('Hello',cli_addr)

    while True:
        data =cli_sock.recv(1024).decode() #把bytes类型解码为str类型
        if data.strip()=='quit':
            break
        print(data)
        sdata = '%s time: %s\r\n' %(data.strip(),time.strftime('%H:%M:%S'))
        cli_sock.send(sdata.encode()) #将str编码为bytes

    cli_sock.close()

s.close()