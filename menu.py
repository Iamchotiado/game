import pygame
from pygame.locals import *
import os
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "freesansbold.ttf"

def main_menu():
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                        menu = False
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(green)
        title=text_format("PLAY WARS", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 45, white)
        else:
            text_start = text_format("START", font, 45, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 45, white)
        else:
            text_quit = text_format("QUIT", font, 45, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - 50, 40))
        screen.blit(text_start, (screen_width/2 + 120, 460))
        screen.blit(text_quit, (screen_width/2 + 120, 510))
        # screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        # screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        # screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))

        playerPNG= pygame.image.load(os.path.join("images","player.png"))
        playerImage=pygame.transform.scale(playerPNG,(155, 165))
        screen.blit(playerImage,(250, 190))

        playerPNG= pygame.image.load(os.path.join("images","archer.png"))
        playerImage=pygame.transform.scale(playerPNG,(155, 165))
        screen.blit(playerImage,(530, 190))

        playerPNG= pygame.image.load(os.path.join("images","armor.png"))
        playerImage=pygame.transform.scale(playerPNG,(155, 165))
        screen.blit(playerImage,(810, 190))

        # player names

        player1_name=text_format("SHOOTER", font, 25, black)
        screen.blit(player1_name, (265, 150))

        player2_name=text_format("ARCHER", font, 25, black)
        screen.blit(player2_name, (545, 150))

        player3_name=text_format("BOMBER", font, 25, black)
        screen.blit(player3_name, (825, 150))

        # player stats

        player1_life=text_format("Powerfull bullet", font, 15, white)
        screen.blit(player1_life, (280, 370))
        player1_power=text_format("Don't worry about gravity!", font, 15, white)
        screen.blit(player1_power, (280, 390))

        player2_life=text_format("Insane damage,", font, 15, white)
        screen.blit(player2_life, (560, 370))
        player2_power=text_format("Little amount of life", font, 15, white)
        screen.blit(player2_power, (560, 390))

        player3_life=text_format("Explotions reach multiple enemies,", font, 15, white)
        screen.blit(player3_life, (820, 370))
        player3_power=text_format("but It does no make many damage.", font, 15, white)
        screen.blit(player3_power, (820, 390))
        player3_last=text_format("Big amiunt of life!", font, 15, white)
        screen.blit(player3_power, (820, 390))

        
        
        pygame.display.update()
        
        pygame.display.set_caption("PLAY WARS")