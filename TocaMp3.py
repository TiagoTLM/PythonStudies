# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3 (dentro da pasta do programa).

import pygame
pygame.init()
# coloca o nome do arquivo que está na pasta do projeto entre aspas
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()
