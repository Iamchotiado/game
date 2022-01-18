import pygame
import os
from player import Player
from parameters import player_type
import parameters
import time

class Game:
    def __init__(self, background, level):
        WIDTH , HEIGHT= 1200,600
        self.WHITE=(255,255,255)
        self.WIN = pygame.display.set_mode((WIDTH , HEIGHT))#display the window
        self.players = []
        self.enemies = []
        self.background = background
        self.level = level
        self.initial_x_p = 100
        self.initial_y_p = 500
        self.initial_x_e = 900
        self.initial_y_e = 500
        self.life_placing = 490
        self.shooter_aiming = 0
        self.playerTurn= True
        self.playersAlive= []
        self.enemiesAlive= []
        self.boss = 0

    def draw_player(self, player):
        if player.is_enemy == False and player.alive == True:
            self.initial_x_p += 80
            self.WIN.blit(player.photo,(player.x, player.y)) 
            


        elif player.is_enemy == True and player.alive== True:
            self.WIN.blit(player.photo,(player.x, player.y))
            self.initial_x_e += 60

    def set_players(self):
            playerPNG= pygame.image.load(os.path.join("images","player.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player1= Player(0, self.WIN, False, player_type[1], 100, 100,  self.initial_x_p, self.initial_y_p, playerImage, True, 30)
            player1.setBullet()
            self.draw_player(player1)

            playerPNG= pygame.image.load(os.path.join("images","archer.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player2= Player(1, self.WIN, False, player_type[2], 100, 100, self.initial_x_p, self.initial_y_p, playerImage, True, 30)
            player2.setBullet()
            self.draw_player(player2)

            playerPNG= pygame.image.load(os.path.join("images","armor.png"))
            playerImage=pygame.transform.scale(playerPNG,(65, 55))
            player3= Player(2, self.WIN, False, player_type[3], 100, 100, self.initial_x_p, self.initial_y_p, playerImage, True, 30)
            player3.setBullet()
            self.draw_player(player3)

            enemyPNG=  pygame.image.load(os.path.join("images","enemy1.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(65, 55))
            enemy1= Player(0, self.WIN, True, player_type[1], 30, 30, self.initial_x_e, self.initial_y_e, enemyImage, True, 10)
            enemy1.setBullet()
            self.draw_player(enemy1)
            
            enemyPNG=  pygame.image.load(os.path.join("images","enemy1.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(75, 55))
            enemy2= Player(1, self.WIN, True, player_type[1], 30, 30, self.initial_x_e, self.initial_y_e, enemyImage, True, 10)
            enemy2.setBullet()
            self.draw_player(enemy2)

            enemyPNG=  pygame.image.load(os.path.join("images","enemy1.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(75, 55))
            enemy3= Player(1, self.WIN, True, player_type[1], 30, 30, self.initial_x_e, self.initial_y_e, enemyImage, False, 100)
            enemy3.setBullet()
            self.draw_player(enemy3)
            


            self.enemies.append(enemy3)            
            self.players.append(player1)
            self.players.append(player2)
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)
            self.players.append(player3)



    
    def draw_window(self):
        self.WIN.fill(self.WHITE) #give the window a colour (blank in this case). look RGP to change it  to another colour
        #use to update any change, if you dont yopu will not see any changes  when you run it
        self.WIN.blit(self.background,(0,0))


    def redraw_window(self):
        self.WIN.fill(self.WHITE) 
        self.WIN.blit(self.background,(0,0))
        add = 40
        for player in self.players:
            if player.alive== True:
                self.WIN.blit(player.photo,(player.x, player.y))
            player.barY += add
            player.barHealth()
            logo=pygame.transform.scale(player.photo, (25, 20))
            self.WIN.blit(logo,(player.barX, player.barY))
            player.barY -= add
            add += 40
            if player.id == self.shooter_aiming  and player.bullet.shoot == True: # to display the bullet
                self.WIN.blit(player.bullet.image,(player.bullet.x, player.bullet.y))
        add= 40
        for enemy in self.enemies:
            if enemy.alive== True:
                self.WIN.blit(enemy.photo,(enemy.x, enemy.y))
            enemy.barX = 1150
            enemy.barY += add
            logo=pygame.transform.scale(enemy.photo, (25, 20))
            if enemy.alive== True:
                enemy.barHealth()
                self.WIN.blit(logo,(enemy.barX-25, enemy.barY))
            enemy.barY -= add
            add += 40
            if enemy.bullet.shoot == True:# to display the bullet and enemy.id == self.shooter_aiming, try to add this later
                self.WIN.blit(enemy.bullet.image,(enemy.bullet.x, enemy.bullet.y))
            
            

    def playerChoice(self):  # to change the player that is going to make the next shoot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.shooter_aiming >0 :
            self.shooter_aiming -= 1
            pygame.time.delay(100) # it will change to fast between one player an another without this 
        elif keys[pygame.K_RIGHT] and self.shooter_aiming < len(self.players)-1 :
            self.shooter_aiming += 1
            pygame.time.delay(100) 
        

    def nextAlive(self): #looks for the next player alive
        levelOver= True
        gameOver = True
        if self.playerTurn == False:
            for player in self.players:
                if player.alive== True:
                    shooter_aiming = self.players.index(player)
                    gameOver= False
        elif self.playerTurn == True:
            for enemy in self.enemies:
                if enemy.alive == True:
                    shooter_aiming = self.enemies.index(enemy)
                    levelOver= False
        if levelOver == True:
            self.level += 1
            self.levels()
        
        
    def got_hit(self):
        if self.playerTurn == True:
            for enemy in self.enemies:
                if enemy.x-50 < self.players[self.shooter_aiming].bullet.x < enemy.x+50 and  enemy.y - 50 < self.players[self.shooter_aiming].bullet.y < enemy.y +50:
                    if enemy.alive== True:
                        enemy.life -= self.players[self.shooter_aiming].damage
                        self.players[self.shooter_aiming].bullet.shoot = False
                        if enemy.life > 0:
                            enemy.alive = True
                        else:
                            enemy.alive= False
                            self.nextAlive()

        elif self.playerTurn == False:
            for player in self.players:
                if player.x-50 < self.enemies[self.shooter_aiming].bullet.x < player.x+50 and  player.y - 50 < self.enemies[self.shooter_aiming].bullet.y < player.y +50: 
                    if player.alive== True:
                        player.life -= self.enemies[self.shooter_aiming].damage
                        self.enemies[self.shooter_aiming].bullet.shoot = False
                        if player.life > 0:
                            player.alive= True
                        else:
                            player.alive = False
                            self.nextAlive()



    def levels(self):
        enemyPNG=  pygame.image.load(os.path.join("images","wizard.png"))
        enemyImage=pygame.transform.scale(enemyPNG,(75, 55))
        shoot1 = pygame.image.load(os.path.join("images","fireball.png"))
        shoot1=pygame.transform.scale(shoot1,(50, 50))
        if self.level == 2: 
            for enemy in self.enemies:
                enemy.alive= True
                enemy.life = 30
                enemy.damage= 30
                enemy.photo = enemyImage
                enemy.bullet.image = shoot1
        
        if self.level == 3:
            enemyPNG=  pygame.image.load(os.path.join("images","boss.png"))
            enemyImage=pygame.transform.scale(enemyPNG,(80, 70))
            self.boss= Player(1, self.WIN, True, player_type[4], 30, 30, 900, self.initial_y_e, enemyImage, True, 100) #create de object
            self.boss.setBullet()
            self.draw_player(self.boss)
            self.enemies = []
            self.enemies.append(self.boss)
            self.shooter_aiming = 0