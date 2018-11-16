import time
import socket

class TcpTimeServer:
    def __init__(self,host='',port=12345):
        self.addr = (host,port)
        self.serv = socket.socket(type=socket.SOCK_STREAM)
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self,cli_sock):
        while True:
            data= cli_sock.recv(1024).decode()
            if data.strip() == 'quit':
                break
            #print(data)
            data = '%s time: %s\r\n' % (data.strip(), time.strftime('%H:%M:%S'))
            cli_sock.send(data.encode())  # 将str编码为bytes

        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock,cli_addr =self.serv.accept() #接收的是一个两元素元组,cli_addr取的是后面的值,等于客户端的ip地址和端口
            except KeyboardInterrupt:
                print()
                break
            self.chat(cli_sock)

        self.serv.close()

if __name__ == '__main__':
    TcpTimeServer().mainloop()