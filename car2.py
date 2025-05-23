import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()  # Creates variable for clock speed
                             # (speed at which car moves)

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Race Game")

# colour
black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
red = (255, 51, 51)

# fonts
exit_font = pygame.font.Font("freesansbold.ttf", 20)  
score_font = pygame.font.SysFont("arialblack", 20)


quit_game = False # The game loop
game_over = False

# x and y coordinate
x = 250
y = 100

car_size = 20

car1_image = pygame.image.load("car_1.png").convert_alpha()
#car1_image = pygame.transform.scale(car1_image, [20, 20])
car1_image = pygame.transform.scale(car1_image, (car_size, car_size))


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




def draw_car(x,y): # now only takes x and y
    screen.blit(car_1.png, (x,y)) # draw the llama image at the given position


def game_loop():
    quit_game = False
    game_over = False  

    car1_x = 250   # x-coordinate for snake
    car1_y = 100   # y-coordinate for snake

    car1_x_change = 0  # Holds value of change in snake x-coordinate
    car1_y_change = 0  # Holds value of change in snake y-coordinate


    while not quit_game: #or While True:
        # When player dies, they are asked if they want to quit or
        # play again 
        while game_over == True:
            save_high_score(high_score)
            screen.fill(white)
            message ("You died! Press Q to Quit or A to Play Again.", black,
                        white)
            score = car1_length - 1 # Added in LA 3.1
            display_scores(score, dark_green, high_score) # Added in LA 3.1
            pygame.display.update()
            for event in pygame.event.get(): # receives all events from the user
                if event.type == pygame.QUIT: # Checks if the event type is a QUIT event. #pygame.QUIT is a predefined Pygame constant.
                    quit_game = True
                    game_over = False
                if event.key == pygame.K_a:
                    game_loop()

                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car1_x_change = -20
                    car1_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    car1_x_change = 20
                    car1_y_change = 0

        # Collision detection (for walls)
        if car1_x >= 1000 or car1_x < 0 or car1_y >= 720 or \
        car1_y < 0:
            game_over = True 
        
        car1_x += car1_x_change
        car1_y += car1_y_change

        screen.fill(grey)           

        clock.tick(120)
        pygame.display.update()

    pygame.quit()
    quit()

game_loop()   # Calls main game loop