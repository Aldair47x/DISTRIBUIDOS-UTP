#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

s = socket.socket()
s.bind(("192.168.9.86", 4002))
s.listen(1)

sc, addr = s.accept()
print "Hola, soy el SERVIDOR"
while True:
      recibido = sc.recv(1024)
      mensaje = "Hola " + recibido
      print "Recibido:", recibido
      lista = ["usuario","contraseña"]
      sc.send(mensaje+"\n"+"Ingrese su usuario")
      user = sc.recv(1024)
      sc.send("Ingrese su contraseña")
      password =  sc.recv(1024)
      if(user==lista[0] and password==lista[1]):
          sc.send("Sus datos son correctos ")
      else:
          sc.send("Sus datos son incorrectos ")
      #sc.send("Sus datos son: "+user+" "+password)
      #sc.send(mensaje)
      break

print "Pasalo bien"

sc.close()
s.close()
