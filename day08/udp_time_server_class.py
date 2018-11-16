import socket,time

class udp_server:
    def __init__(self,host='',port=12345):
        self.addr =(host,port)
        self.serv = socket.socket(type=socket.SOCK_DGRAM)
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)

    def chat(self):
        while True:
            try:
                data,cli_addr=self.serv.recvfrom(1024)
            except KeyboardInterrupt:
                print('\nBye-bye')
                break
            data = data.decode().strip()
            if data == 'quit':
                break
            print(data)
            data = '[%s] %s\r\n' % (time.strftime('%H:%M:%S'), data.strip())
            self.serv.sendto(data.encode(), cli_addr)

        self.serv.close()

if __name__ == '__main__':
    udp_server().chat()