import socket, select

def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            socket.send(message)

            
if __name__ == "__main__":

    CONNECTION_LIST = []
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("192.168.61.194", 8000))
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)

    print "#### SERVIDOR EN LINEA ####"

    while True:
        read_sockets,_,_ = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "### Cliente (%s, %s) conectado" % addr

                broadcast_data(sockfd, "[%s:%s] Conectado\n" % addr)

            else:
                data = sock.recv(4096)
                broadcast_data(sock, "\r" + '[' + str(sock.getpeername()) + ']' + '==>> ' + data)


    server_socket.close()
