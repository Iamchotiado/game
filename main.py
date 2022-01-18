import imp
import pygame
import os
from game import Game
from player import Player
from bullet import Bullet
import parameters
import time
import random
from menu import main_menu
FPS= 60
#create de characters
#game.enemies[random.randrange(0, 1)].shooting()

player_type = {0: 'shooter', 1:'archer', 2:'bomber'}



WIDTH , HEIGHT= 1200,600
WIN = pygame.display.set_mode((WIDTH , HEIGHT))#display the window
WHITE=(255,255,255)
RED= (255,0,0)
FPS=20
black= (0,0,0)
background1= pygame.transform.scale(pygame.image.load(os.path.join("images","background.png")),(WIDTH,HEIGHT))
    
def main():
    main_menu()
    clock=pygame.time.Clock()
    run = True
    game = Game(background1, 1)
    game.draw_window()
    game.set_players()
    while run== True:
        clock.tick(FPS)#run the while loop 60 tme per second
        if game.playerTurn == True:
            game.playerChoice()
            for event in pygame.event.get():#list of all the differents event, looping trhough them
                if event.type == pygame.QUIT:
                    run=False
                elif event.type== pygame.MOUSEBUTTONDOWN and game.players[game.shooter_aiming].bullet.shoot == False :
                    game.players[game.shooter_aiming].anglePower() # will made the shoot
                    while game.players[game.shooter_aiming].bullet.shoot == True:
                        game.got_hit()
                        game.players[game.shooter_aiming].bulletPosition() # update the bullet position
                        if game.players[game.shooter_aiming].bullet.shoot == False:
                            game.playerTurn = False
                            pygame.time.delay(1000)   
                        game.redraw_window()    
                        pygame.display.update()
                pygame.event.clear()


            game.redraw_window()    
            #pygame.display.update()
            game.players[game.shooter_aiming].aim()

            
        elif game.playerTurn == False:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
            game.shooter_aiming = random.randrange(0, len(game.enemies)) 
            game.enemies[game.shooter_aiming].anglePower()
            #print(game.enemies[game.shooter_aiming].bullet.power)
            while game.enemies[game.shooter_aiming].bullet.shoot == True:
                game.got_hit()
                game.enemies[game.shooter_aiming].bulletPosition() # update the bullet position
                if game.enemies[game.shooter_aiming].bullet.shoot == False:
                    game.playerTurn = True
                game.redraw_window()    
                pygame.display.update()
            game.redraw_window()    
            pygame.display.update()
            pygame.event.clear()

        
        
        pygame.display.update()#use to update any change, if you dont you will not see any changes  when you run it 
    pygame.quit()       


main()
