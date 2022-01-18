import pygame
import os
from bullet import Bullet
import parameters
import math
import random 
import sys

class Player:
    def __init__(self, id, WIN, is_enemy, player_type, life, maxLife, x, y, photo, alive, damage,):
        self.id = id
        self.WIN=WIN
        self.is_enemy = is_enemy
        self.player_type = player_type
        self.life = life
        self.maxLife = maxLife
        self.x = x
        self.y = y
        self.photo = photo
        self.alive = alive
        self.bullet = 0
        self.damage = damage 
        self.barX = 20
        self.barY = 0


    def aim(self):
        if self.alive== True:
            black= (0,0,0)
            mx,my = pygame.mouse.get_pos()
            mouse=[mx, my]
            if mouse[0]<self.x+300 and mouse[1]>300:
                pygame.draw.polygon(self.WIN,black, ((self.x+25,515), (self.x+25, 520), (mouse[0], mouse[1]+5),(mouse[0]-5, mouse[1])))
                aim= pygame.image.load(os.path.join("images","aim.png"))
                aim=pygame.transform.scale(aim,(65, 55))
                self.WIN.blit(aim,(mouse[0]-30,mouse[1]-30 ))

    def setBullet(self):
        
        if self.player_type == parameters.player_type[1]:
            shoot1 = pygame.image.load(os.path.join("images","bullet2.png"))
            shoot1=pygame.transform.scale(shoot1,(80, 80))
            shoot1= Bullet(shoot1, self.x, self.y,0,0, False)
            self.bullet = shoot1

        elif self.player_type == parameters.player_type[2]:
            shoot1 = pygame.image.load(os.path.join("images","arrow.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y, 0, 0, False)
            self.bullet = shoot1

        elif  self.player_type == parameters.player_type[3]:
            shoot1 = pygame.image.load(os.path.join("images","granade.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y, 0, 0, False)
            self.bullet = shoot1

        elif  self.player_type == parameters.player_type[4]:
            shoot1 = pygame.image.load(os.path.join("images","spirit.png"))
            shoot1=pygame.transform.scale(shoot1,(50, 50))
            shoot1= Bullet(shoot1, self.x, self.y, 0, 0, False)
            self.bullet = shoot1

    def ballpath(self):
        power= self.bullet.power
        angle= self.bullet.angle
        time= self.bullet.time
        #using suvat equations
        velX=math.cos(angle) * power # horizontal velocity
        velY= math.sin(angle) * power # vertical velocity
        distX=  velX * time  # constant velocity 
        distY= (velY * time) + ((-4.9 * (time)**2)) # -4.9 is the gravity/2

        newX= round(distX+ self.bullet.x)
        newY = round(self.bullet.y- distY)
        return (newX, newY)   #this is a tuple
    
    def findAngle(self):
        if self.is_enemy== False:
            mx,my = pygame.mouse.get_pos()
            mouse=[mx, my]
        elif self.is_enemy == True: 
            mx,my = pygame.mouse.get_pos()
            mouse=[mx, my]
        aX= self.x
        aY= self.y
        if aX == mouse[0]:
            angle=math.pi / 2
        else: 
            angle= math.atan((aY - mouse[1]) / (aX - mouse[0]))# atan give you an angle, the line will give you the angle of the player and the aming
        #pendiente ,diferencia de y / diferencia de x
        if mouse[1] > aY and mouse[0]> aX: #first cuadrantant
            angle = (math.pi * 2) -angle
        elif mouse[1] > aY and mouse[0] < aX: #second cuadrant 
            angle= math.pi + abs(angle)
        elif mouse[1] < aY and mouse[0] < aX: #third cuadrant
            angle=math.pi - abs(angle)
        elif mouse[1] < aY and mouse[0] > aX: #forth cuadrant
            angle= abs(angle)
        return angle
    
    def bulletPosition(self):
            if self.bullet.y < 600 and 0 <self.bullet.x < 1200 and self.bullet.shoot == True:
                pygame.time.delay(15)
                self.bullet.time+= 0.05
                position= self.ballpath()
                self.bullet.x= position[0]
                self.bullet.y= position[1]
            else: 
                self.bullet.shoot = False
                self.bullet.x = self.x
                self.bullet.y = self.y
                self.bullet.time= 0



    def anglePower(self):
        
        if self.bullet.shoot== False and self.alive == True:
            self.bullet.shoot=True
            x= self.bullet.x
            y= self.bullet.y
            if self.is_enemy== False:
                mx,my = pygame.mouse.get_pos()
                mouse=[mx, my]
            else:
                randomX= random.randrange(self.x-50, self.x-30)
                randomY= random.randrange(self.y-100, self.y-90)
                mouse=[randomX, randomY]

            self.bullet.power = math.sqrt((mouse[1]-y)**2+ (mouse[0]-x)**2)/8
            #distance between 2 roots: square root of changing x + changing y    / ((x2-x1)+(y2-y1))**1/2
            if x == mouse[0]:
                angle=math.pi / 2
            else: 
                angle= math.atan((y - mouse[1]) / ( x - mouse[0])) # atan give you an angle, the line will give you the angle of the player and the aming
            if mouse[1] > y and mouse[0]> x: #first cuadrantant
                angle = (math.pi * 2) -angle
            elif mouse[1] > y and mouse[0] < x: #second cuadrant 
                angle= math.pi + abs(angle)
            elif mouse[1] < y and mouse[0] < x: #third cuadrant
                angle=math.pi - abs(angle)
            elif mouse[1] < y and mouse[0] > x: #forth cuadrant
                angle= abs(angle)
            self.bullet.angle = angle


    def barHealth(self):
        green=(0,255, 0)
        barLenght=400
        healthRatio = self.maxLife/ barLenght
        width= round(self.life/healthRatio)
        self.barPosition=  20
        if self.is_enemy== False:
            pygame.draw.polygon(self.WIN,(0,0,0), ((self.barX, self.barY), (self.barX, self.barY+20),(self.barX+ barLenght, self.barY+20), (self.barX+ barLenght,self.barY ))) # show the max life 
            pygame.draw.polygon(self.WIN,(green), ((self.barX, self.barY),(self.barX, self.barY+20),(self.barX + width, self.barY +20), (self.barX+width, self.barY ))) #show the life left 
        else:
            pygame.draw.polygon(self.WIN,(0,0,0), ((self.barX- barLenght, self.barY), (self.barX - barLenght, self.barY+20),(self.barX, self.barY+20), (self.barX,self.barY ))) # show the max life 
            pygame.draw.polygon(self.WIN,(green), ((self.barX- width, self.barY),(self.barX- width, self.barY+20),(self.barX, self.barY +20), (self.barX, self.barY ))) #show the life left 



        
        #pygame.draw.rect(self.WIN,(255,0,0),10,10,width,25) # 10, 10 are the position , 25 is the height 
        #pygame.draw.rect(self.WIN,(255,255,255),barLenght)



    def getHealth(self): 
        if self.life < self.maxLife:
            self.life =+ maxlife/10 #add 10 porcent of the health
            #take money
            if self.life > self.maxLife:
                self.life = self.maxLife
