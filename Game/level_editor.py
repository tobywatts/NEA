import pygame
import time

from level_events import EventManager
from level_renderer import Renderer
from level_settings import *

eventManager = EventManager()
renderer = Renderer()

pygame.init()

start_time = time.time()
delta_time = 0

eventManager.store_tiles()
eventManager.world()
renderer.tile_buttons(eventManager)
eventManager.load_level(renderer)

while eventManager.running:

    new_time = time.time()

    if new_time - start_time >= 1 / FPS:
        delta_time = (new_time - start_time)
        start_time = new_time

        renderer.draw_bg()
        renderer.draw_grid()
        renderer.draw_world(eventManager)
        eventManager.check_scroll(renderer, delta_time)

    eventManager.check_events()
    eventManager.tile_placing(renderer)

    pygame.draw.rect(renderer.win, (50, 180, 125), (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    eventManager.save_level(renderer)

    for button_count, i in enumerate(button_list):
        if i.draw(renderer.win):
            eventManager.current_tile = button_count

    pygame.draw.rect(renderer.win, (255, 255, 255), button_list[eventManager.current_tile], 2)

    pygame.display.update()
