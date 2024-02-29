from ursina import *
from ursina import collider 
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint, uniform
import time

app = Ursina() 

player = FirstPersonController(model = 'cube',
                               jump_height = 0, 
                               gravity = 1, 
                               speed = 3, 
                               position = (-49, 0, -49),
                               collider = 'box'
) 

floor = Entity(model = 'plane',  
              collider = 'box', 
              scale = (100, 1, 100), 
              texture = 'grass') 

wall1 = Entity(model = 'cube',
              collider = 'box', 
              position = (0, 0, -50), 
              scale = (100, 10, 0), 
              color = color.gray)

wall2 = Entity(model = 'cube',
              collider = 'box', 
              position = (-50, 0, 0), 
              scale = (0, 10, 100), 
              color = color.gray)

wall3 = Entity(model = 'cube',
              collider = 'box', 
              position = (50, 0, 0), 
              scale = (0, 10, -100), 
              color = color.gray)

wall4 = Entity(model = 'cube',
              collider = 'box', 
              position = (0, 0, 50), 
              scale = (-100, 10, 0), 
              color = color.gray)
    
sky = Sky(texture = 'sky_sunset') 
frame_counter = 0
obstacles = []
coins = []
coin_counter = 0
finished = []
points = 0

def update():
    global frame_counter, obstacles, coin_counter, coins
    frame_counter += 1

    if held_keys['c']:
        application.pause()
        mouse.locked = False
        message = Text(text = 'Game over', origin = (0, 0), background = True, color = color.green)
    
    aim = Text(text = 'Collect 5 coins before going to the red box as fast as possible. Do not collide with blue obstacles!' , background = True, scale = 0.8, x = -0.4, y = .4, color = color.white)
    stopwatch = Text(text = "Stopwatch : ", origin = (5,5))

    if frame_counter % 60 ==0:
        time_counter = Text(text = str(frame_counter//60), origin = (42, 5))
        time_counter.fade_out(0, 1)
    
    if frame_counter == 10:
        coin = Entity(model = 'sphere',  
                  scale = (1, 1, 1), 
                  color = color.yellow, 
                  position = (randint(-49, 49), 1, -40),
                  collider = 'box')
        coin2 = Entity(model = 'sphere',  
                  scale = (1, 1, 1), 
                  color = color.yellow, 
                  position = (randint(-49, 49), 1, -20),
                  collider = 'box')
        coin3 = Entity(model = 'sphere',  
                  scale = (1, 1, 1), 
                  color = color.yellow, 
                  position = (randint(-49, 49), 1, 0),
                  collider = 'box')
        coin4 = Entity(model = 'sphere',  
                  scale = (1, 1, 1), 
                  color = color.yellow, 
                  position = (randint(-49, 49), 1, 20),
                  collider = 'box')
        coin5 = Entity(model = 'sphere',  
                  scale = (1, 1, 1), 
                  color = color.yellow, 
                  position = (randint(-49, 49), 1, 40),
                  collider = 'box')
        finish = Entity(model = 'cube',
              collider = 'box', 
              position = (randint(-49, 50), 0, 48), 
              scale = (3, 7, 3), 
              color = color.red) 
        coins.append(coin)
        coins.append(coin2)
        coins.append(coin3)
        coins.append(coin4)
        coins.append(coin5)
        finished.append(finish)

    if frame_counter % 90 == 0:
        obstacle = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, -45),
                  collider = 'box')
        obstacle2 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, -35),
                  collider = 'box')
        obstacle3 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, -25),
                  collider = 'box')
        obstacle4 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, -15),
                  collider = 'box')
        obstacle5 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, -5),
                  collider = 'box')
        obstacle6 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, 5),
                  collider = 'box')
        obstacle7 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, 15),
                  collider = 'box')
        obstacle8 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, 25),
                  collider = 'box')
        obstacle9 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, 35),
                  collider = 'box')
        obstacle10 = Entity(model = 'cube',  
                  scale = (5, 4, 1), 
                  color = color.blue, 
                  position = (-50, 0, 45),
                  collider = 'box')
        obstacles.append(obstacle)
        obstacles.append(obstacle2)
        obstacles.append(obstacle3)
        obstacles.append(obstacle4)
        obstacles.append(obstacle5)
        obstacles.append(obstacle6)
        obstacles.append(obstacle7)
        obstacles.append(obstacle8)
        obstacles.append(obstacle9)
        obstacles.append(obstacle10)

    for obstacle in obstacles:
        obstacle.x += uniform(0.05, 0.2)
        hit_info = obstacle.intersects()
        if hit_info.hit:
            if hit_info.entity == player:
                application.pause()
                mouse.locked = False
                message = Text(text = 'Game over', origin = (0, 0), background = True, color = color.green)
    
    for coin in coins:
        hit_info = coin.intersects()
        if hit_info.hit:
            if hit_info.entity == player:
                destroy(coin)
                coin_counter += 1

    for finish in finished:
        hit_finish = finish.intersects()
        if hit_finish.hit:
            if hit_finish.entity == player and coin_counter == 5:
              application.pause()
              mouse.locked = False
              message = Text(text = "You won", origin = (0, 0), background = True, color = color.green)
        if hit_finish.entity == player and coin_counter < 5:
             message = Text(text = 'Please collect all 5 coins ', origin = (0, 0), background = False, color = color.white)
             message.fade_in(0,1)  


app.run() 