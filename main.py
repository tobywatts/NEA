import pygame
import time

from events import EventManager
from renderer import Renderer
from settings import *
from player import Player

eventManager = EventManager()
renderer = Renderer()
player = Player()

pygame.init()

start_time = time.time()
delta_time = 0

eventManager.store_tiles()
eventManager.world()
eventManager.load_level(renderer)

while eventManager.running:

    new_time = time.time()

    if new_time - start_time >= 1 / FPS:
        delta_time = (new_time - start_time)
        start_time = new_time

        player.move(eventManager, renderer, delta_time)
        renderer.draw_bg()
        renderer.draw_world(eventManager)
        # renderer.draw_hitbox(eventManager)
        player.shoot(renderer)
        player.draw(renderer)



    eventManager.check_events()

    pygame.display.update()