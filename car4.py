import pygame
import time
import random

pygame.init()

width = 500
height = 800
screen = pygame.display.set_mode((width, height))
#clock = pygame.time.Clock()  # Creates variable for clock speed
                             # (speed at which car moves)

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Race Game")

# colour
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)
red = (255, 51, 51)
green = (0, 153, 0)
yellow = (255, 255, 51)

# fonts
exit_font = pygame.font.Font("freesansbold.ttf", 20)  
score_font = pygame.font.SysFont("arialblack", 20)


#quit_game = False # The game loop
#game_over = False

# x and y coordinate
#x = 250
#y = 100

# setting
game_over = False
speed = 2
score = 0

# image
car1 = pygame.image.load("car_1.png")
car2 = pygame.image.load("car_2.png")
car3 = pygame.image.load("car_3.png")
car4 = pygame.image.load("car_4.png")
car5 = pygame.image.load("car_5.png")
car6 = pygame.image.load("car_6.png")

# markers size
marker_width = 10
marker_height = 50

# road and edge markers
road = (50, 0, 400, height)
left_edge_marker = (50, 0, marker_width, height)
right_edge_marker = (440, 0, marker_width, height)

# x coordinates of lanes
left_lane = 100
center_lane = 200
right_lane = 300
lanes = [left_lane, center_lane, right_lane]

# for animating movement of the lane markers
lane_marker_move_y = 0

fps = 60 # cannot run faster than 60
run = True
clock = pygame.time.Clock() # Creates variable for clock speed

while run: # Main event loop
    clock.tick(fps) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # window will be closed if user press the X
            run = False
            break

    screen.fill(green)

    # draw the road
    pygame.draw.rect(screen, gray, road)

    # draw the edge markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # draw the lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
      lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
      pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
      pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
      pygame.draw.rect(screen, white, (right_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    pygame.display.update()

pygame.quit() # Exit the while loop and then Quit the game 

#6:29
#1 #13:04
#koko

def load_high_score():
    """Checks if HI_score.txt file exists. If it doesn't, creates file
    and writes the value 0 to the file.
    Then it sets the variable named value as the value read from the 
    file and returns it.
    """
    try:
      hi_score_file = open("HI_score.txt", 'r')
    except:
      hi_score_file = open("HI_score.txt", 'w')
      hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value

def update_high_score(score, high_score):
    """Added in Learning Activity 3.2.
    Checks whether current score is greater than high score and,
    if so, updates high score. Otherwise, high score is returned as
    updated high score."""
    if(int(score) > int(high_score)):
      return score
    else:
      return high_score


def display_scores(score, score_colour, high_score):
    """Displays current score and high score throughhout the game.
    """
    # Current score:
    display_score = score_font.render("Score: " + str(score), True, 
    score_colour)
    screen.blit(display_score, (500-140,10))

    # High score:
    display_score = score_font.render("HIGH SCORE: " + str(high_score), 
    True, score_colour)
    screen.blit(display_score, (10,10))


def save_high_score(high_score):
    """Added in Learning Activity 3.2.
    Saves the updated high score when the program is exited."""
    hi_score_file = open("HI_score.txt", 'w')
    hi_score_file.write(str(high_score))
    hi_score_file.close()


def message(msg,txt_colour, bkgd_colour):
    txt = exit_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center = (500, 360))
    screen.blit(txt, text_box)


#game_loop()   # Calls main game loop