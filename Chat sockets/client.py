import socket, select, string, sys

def prompt() :
    sys.stdout.write('#[TU]: ')
    sys.stdout.flush()

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect(("192.168.61.194", 8000))

    print '### CONECTADO, Ahora puedes enviar un mensaje ! ###'
    prompt()

    while True:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                sys.stdout.write(data)
                prompt()
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
