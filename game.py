#-*- coding:utf-8 -*-
import pygame
import time
import sys
import socket

host = "192.168.1.35"
port = 5003
buf = 15
calistir = (host,port)
istemci = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
istemci.connect(calistir)

pygame.init()
pygame.display.set_mode((100,100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("solshift")
                continue
            if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("sagshift")
                continue

            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send( "yukarishift")
                continue

            if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send( "asagishift")
                continue

            if event.key == pygame.K_LEFT:
                istemci.send( "sol")

            if event.key == pygame.K_RIGHT:
                istemci.send( "sag")

            if event.key == pygame.K_UP:
                istemci.send( "yukari")

            if event.key == pygame.K_r:
                istemci.send( "r")

            if event.key == pygame.K_DOWN:
                istemci.send( "asagi")

            if event.key == pygame.K_SPACE:
                istemci.send("duzelt")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                istemci.send( "kapat")
                time.sleep(1)
                istemci.close()
                sys.exit(0)

            if event.key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("up") #( "solshift_")
                continue
            if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("up") #( "sagshift_")
                continue

            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("up") #( "yukarishift_")
                continue

            if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                istemci.send("up") #( "asagishift_")
                continue

            if event.key == pygame.K_LEFT:
                istemci.send("up") #( "sol_")

            if event.key == pygame.K_RIGHT:
                istemci.send("up") #( "sag_")

            if event.key == pygame.K_UP:
                istemci.send("up") #( "yukari_")

            if event.key == pygame.K_DOWN:
                istemci.send("up") #( "asagi_")

            if event.key == pygame.K_r:
                istemci.send("up") #( "r_")
