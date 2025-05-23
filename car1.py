import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Race Game")

exit_font = pygame.font.Font("freesansbold.ttf", 20)  
score_font = pygame.font.SysFont("arialblack", 20)

#colour
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)

quit_game = False #The game loop 

#x and y coordinate

while not quit_game: #or While True:
    for event in pygame.event.get(): #receives all events from the user
        if event.type == pygame.QUIT: #Checks if the event type is a QUIT event. #pygame.QUIT is a predefined Pygame constant.
            quit_game = True     

    clock.tick(120)
    pygame.display.update()

pygame.quit()
quit()