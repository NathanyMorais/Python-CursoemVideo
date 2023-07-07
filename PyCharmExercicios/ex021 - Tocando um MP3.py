# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Resolução do Guanabara:

import pygame  # baixar a biblioteca pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')  # copiar e colar o arquivo mp3 dentro da pasta do projeto "PyCharmExercicios"
pygame.mixer.music.play()
pygame.event.wait()
