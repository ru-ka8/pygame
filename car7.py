import pygame
import time
import random

pygame.init()

width = 600
height = 800
screen = pygame.display.set_mode((width, height))
#clock = pygame.time.Clock()  # Creates variable for clock speed
                             # (speed at which car moves)

game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car Race Game")

# colour
black = (32, 32, 32)
white = (255, 255, 255)
gray = (192, 192, 192)
red = (255, 51, 51)
green = (0, 153, 0)
yellow = (255, 255, 51)

# fonts
exit_font = pygame.font.Font("freesansbold.ttf", 30)  
score_font = pygame.font.SysFont("arialblack", 30)


# setting
game_over = False
speed = 2
score = 0



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
    display_score = score_font.render("SCORE: " + str(score), True, 
    score_colour)
    screen.blit(display_score, (400, 50))

    # High score:
    display_score = score_font.render("HIGH SCORE: " + str(high_score), 
    True, score_colour)
    screen.blit(display_score, (300,10))


def save_high_score(high_score):
    """Added in Learning Activity 3.2.
    Saves the updated high score when the program is exited."""
    hi_score_file = open("HI_score.txt", 'w')
    hi_score_file.write(str(high_score))
    hi_score_file.close()


def message(msg, txt_colour):
    txt = exit_font.render(msg, True, txt_colour)
    text_box = txt.get_rect(center = (width / 2, 250))
    screen.blit(txt, text_box)



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

# class means like dictionally 
class Cars(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        # scale the image down so it fits in the lane
        image_scale = 60 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class PlayersCar(Cars):

    def __init__(self, x, y):
        car1 = pygame.image.load('Assesment/car_1.png') #13:25
        super().__init__(car1, x, y) 

# player's starting coordinates
player_x = 200
player_y = 600

# create the player's car
player_group = pygame.sprite.Group()
player = PlayersCar(player_x, player_y)
player_group.add(player)

# loop the other cars images
#image_filenames = ["carspic"]
image_name = ['car_2.png', 'car_3.png', 'car_4.png', 'car_5.png', 'car_6.png'] #18:20
car_images = []
for image_name in image_name:
  image = pygame.image.load('Assesment/' + image_name)
  car_images.append(image)

# sprite group for cars
car_group = pygame.sprite.Group()



fps = 60 # cannot run faster than 60
quit_game = False
clock = pygame.time.Clock() # Creates variable for clock speed

high_score = load_high_score()

def game_loop():

  while not quit_game: # Main event loop
      clock.tick(fps) 

      while game_over == True:
        save_high_score(high_score)
        pygame.draw.rect(screen, red, (0, 200, width,100))
        message ("You died! Play Again? Enter Y or N", white)
        display_scores(score, black, high_score) # Added in LA 3.1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    quit_game = True
                    game_over = False
                if event.key == pygame.K_y:
                    game_loop()

      for event in pygame.event.get():
          if event.type == pygame.QUIT: # window will be closed if user press the X
              quit_game = True
              break

          # move the player's car using the left/right arrow keys
          if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and player.rect.center[0] > left_lane: #or center_lane
              player.rect.x -= 100
            elif event.key == pygame.K_RIGHT and player.rect.center[0] < 400: # right_lane:
              player.rect.x += 100

              # check if there"s a side swipe collision after changing lanes
              for cars in car_group:
                if pygame.sprite.collide_rect(player, cars):

                  game_over = True


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

      # draw the player's car
      player_group.draw(screen) #14:39

      # add up to two cars
      if len(car_group) < 2:

        # ensure there's enough gap between cars
        add_car = True
        for car in car_group:
          if car.rect.top < car.rect.height * 1.5:
            add_car = False

        if add_car:

          # select a random lane
          lane = random.choice(lanes)

          # select a random car image
          image = random.choice(car_images) # koko
          car = Cars(image, lane, height / -2)
          car_group.add(car)

      # make the cars move
      for car in car_group:
        cars_speed = round(random.randrange(3, 30))
        car.rect.y += cars_speed

        # remove the car once it goes off screen
        if car.rect.top >= height:
          car.kill()

          # add to score
          score += 1

          #speed up the game after passing 5 cars
          if score > 0 and score % 5 == 0:
            speed += 1

      # draw the cars
      car_group.draw(screen) #22:30

      # check if there's a head on collision
      if pygame.sprite.spritecollide(player, car_group, True):
        game_over = True


      high_score = update_high_score(score, high_score)
      display_scores(score, black, high_score) # Added in LA 3.1

        

      pygame.display.update()

  pygame.quit() # Exit the while loop and then Quit the game 

game_loop() # Calls main game loop