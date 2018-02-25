import zmq
import sys
import os
import numpy as np
from io import StringIO
from numpy.linalg import inv
from scipy.linalg import *
import json

def loadFiles(path):
    files = {}
    dataDir = os.fsencode(path)
    for file in os.listdir(dataDir):
        filename = os.fsdecode(file)
        print("Loading {}".format(filename))
        files[filename] = file
    return files

def main():

    if len(sys.argv) != 3:
        print("Must be called with two arguments!")
        exit()

    directory = sys.argv[2]
    port = sys.argv[1]

    context = zmq.Context()
    s = context.socket(zmq.REP)
    s.bind("tcp://*:{}".format(port))
    files = loadFiles(directory)

    while True:
        msg = s.recv_json()
        if msg["op"] == "invertir matriz":
            filename = msg["file"]
            matriz = []
            archivo = open("./files/"+filename, 'r+',encoding='utf-8') 
            for linea in archivo:
                matriz.append(linea.strip().split())
            archivo.close()
            w = open("./files/matrizCliente", 'r+',encoding='utf-8')
            matrizInv=inv(matriz) 
            w.write(str(matrizInv))
            w.write('\n')
            s.send_json({"files": str(matrizInv)})
        else:
            print("Unsupported action!")

if __name__ == '__main__':
    main()

