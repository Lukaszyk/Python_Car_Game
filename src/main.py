import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6) # 800/1,6 = 500
roadmark_w = int(width/80) # 800/80 = 10
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1


pygame.init()
runnin = True
# set window size
SCREEN = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Car game")
# set background colour
SCREEN.fill((60, 220, 0))

# load player vehicle
car = pygame.image.load("Python_Car_Game/img/car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy vehicle
car2 = pygame.image.load("Python_Car_Game/img/otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

# apply changes
pygame.display.update()

counter = 0
# game loop
while runnin:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # animate enemy vehicle
    car2_loc[1] += speed # zmiana położenia autka o 1px z każdym przejściem pętli
    if car2_loc[1] > height:
        #car2_loc[1] = -200 # taka wartość by wyglądało jak by wyjeżdżał z poza ekranu, wartość ta jest podyktowana wielkością grafiki autka
        # polecenie powyżej nie jest już potrzebne ponieważ przy poruszaniu się autka jest ustalona ta wartość
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else: 
            car2_loc.center = left_lane, -200

    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250: # [0] oznacza od pozycji x, [1] oznaczna od pozycji y
        print("GAME OVER! YOU LOST!")
        break



    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            runnin = False
        if event.type == KEYDOWN: # rodzaj zdażenia wciśnięcia przycisku na klawiatrzue
            if event.key in [K_a, K_LEFT]: # jeżeli w zdażeniu przycisku spośród listy przycisków [a oraz strzałka w lewo]
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]: # jeżeli w zdażeniu przycisku spośród listy przycisków [d oraz strzałka w prawo]
                car_loc = car_loc.move([int(road_w/2), 0])


    # draw graphics
    pygame.draw.rect(SCREEN, (50, 50, 50),(width/2-road_w/2, 0, road_w, height))
    pygame.draw.rect(SCREEN, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height)) # żółta linia na środku, koordynaty są odpowiednio x-start, x-end, y-start, y-end
    pygame.draw.rect(SCREEN, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)) #rysowanie białych lini na krawędziach
    pygame.draw.rect(SCREEN, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)) #rysowanie białych lini na krawędziach




    SCREEN.blit(car, car_loc)
    SCREEN.blit(car2, car2_loc)
    pygame.display.update()



pygame.quit()
