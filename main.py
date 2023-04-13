import pygame
import time
import bullet

from events import EventManager
from renderer import Renderer
from settings import *
from player import Player
from enemy import Enemy

eventManager = EventManager(0, 0)
renderer = Renderer()
player = Player(650, 1010)


pygame.init()

start_time = time.time()
delta_time = 0

eventManager.store_tiles()
eventManager.world()
eventManager.load_level(renderer)

enemy_count = 15
enemy_spawn_locations = [(100, 235), (500, 115), (450, 405), (100, 525), (70, 810), (730, 775), (830, 525), (1240, 165), (1150, 405), 
                         (1580, 325), (2080, 560), (1820, 210), (2100, 880), (1800, 1040), (1520, 955)]
chosen_spawn = []
temp_enemies = []
enemies = []

for i in range(enemy_count):
    enemy = Enemy(enemy_spawn_locations[i][0], enemy_spawn_locations[i][1])
    enemies.append(enemy)

pygame.mouse.set_visible(False)
while eventManager.running:

    new_time = time.time()

    if new_time - start_time >= 1 / FPS:
        delta_time = (new_time - start_time)
        start_time = new_time


        for enemy in enemies:
            enemy.move(eventManager, renderer, delta_time, player)

        player.move(eventManager, renderer, delta_time)
        renderer.draw_bg()
        renderer.draw_world(eventManager)

        for bullet in player.bullets:
            deadBullet = bullet.move(delta_time, eventManager)
            if deadBullet:
                player.bullets.remove(bullet)
            bullet.show(renderer)

        # renderer.draw_hitbox(eventManager)
        
        for enemy in enemies:
            if enemy.health <= 0:
                enemies.remove(enemy)

            if enemy.walk == True:
                enemy.walk_animation()

            if enemy.idle == True:
                enemy.idle_animation()
            enemy.show(renderer)

        # player.attack(renderer)
        
        player.draw(renderer, delta_time)
        enemy.attack_player(renderer, player)

        # player.attack(renderer, delta_time, bullet)




    eventManager.check_events(player, renderer)

    pygame.display.update()