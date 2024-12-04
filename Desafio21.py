# Imprime o título do desafio
print('====== DESAFIO 21 ======')

# Faça um programa am Python qua abra a
# reproduza o áudio da um arquivo MP3.

# Inicializa todos os módulos do pygame
import pygame

# Inicializa todos os módulos do pygame
pygame.init()

# Carrega o arquivo de áudio MP3 para reprodução
pygame.mixer.music.load ('loftPy.mp3')

# Inicia a reprodução do áudio
pygame.mixer.music.play()

input() #Na versão atual do pygame precisa do comando input() para fazer a reprodução do audio

# Aguarda o fim da reprodução (para garantir a execução correta em versões específicas do pygame)
pygame.event.wait()
