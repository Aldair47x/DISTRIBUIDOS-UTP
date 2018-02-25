import zmq
import sys
import time

def main():
    if len(sys.argv) != 4:
        print("Must be called with three arguments!")
        exit()
    ip = sys.argv[1]
    port = sys.argv[2]
    operation = sys.argv[3]

    context = zmq.Context()
    s = context.socket(zmq.REQ)
    s.connect("tcp://{}:{}".format(ip,port))

    if operation == "invertir matriz":
        name = input("Name of file: ")
        s.send_json({"op":"invertir matriz", "file":name})
        files = s.recv_json()
        print(files)
    else:
        print("Error")
    print("Connecting to server {} at {}".format(ip,port))

if __name__ == '__main__':
    main()
