#Importações.

import pygame
from pygame.locals import *
from sys import exit
import random

#Criação da variavel de tela , inicialização do pygame , criação da variavel para acelerar os ticks e etc.
imgbg = pygame.image.load("BG.png")
img = pygame.image.load("sprite.png")
img2 = pygame.image.load("sprite2.png")
pontos=0
pygame.init()
tela = pygame.display.set_mode((1024,512))
pygame.display.set_caption("JOGUIN RUIM")
relógio=pygame.time.Clock()
fonte=pygame.sysfont.SysFont("arial",40,True,False)
pygame.font.init()

#Variaveis de coordenadas.

x=512
y=256

b_x=random.randint(a=0,b=1024)
b_y=random.randint(a=0,b=512)
#Loop de verificações e ações.

while True :
    bg=tela.blit(imgbg,(0,0))
    gordo=tela.blit(img,(x,y))
    prato=tela.blit(img2,(b_x,b_y))
    mensagem=f"pontos:{pontos}"
    texto=fonte.render(mensagem,True,(255,255,255))
    tela.blit(texto,(800,60),(0,0,200,50))
    relógio.tick(1000)
    pygame.display.update()
    tela.fill((0,0,0))
    
    
    for event in pygame.event.get() :
    
        #Código para movimentação.
    
        if pygame.key.get_pressed()[K_a] :
            
            x=x-10
        
        if pygame.key.get_pressed()[K_d] :
            
            x=x+10
        
        if pygame.key.get_pressed()[K_w] :
            
            y=y-10
        
        if pygame.key.get_pressed()[K_s] :
            
            y=y+10

        #Colisão entre a bolinha e o player
    
        if gordo.colliderect(prato) :
         
            b_x=random.randint(a=24,b=1024)
            b_y=random.randint(a=24,b=512)
            pontos=pontos+1
        
        #Código para fechar o jogo.
        
        if event.type == QUIT:
            
            pygame.quit()
            exit()
