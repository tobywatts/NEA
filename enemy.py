import pygame

from settings import *


from player import Player


class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.attack = False

        self.up = pygame.math.Vector2(0, 1)

        self.direction = 'left'

        self.vel = 75
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.walk = True
        self.idle = False
        self.attack = False


        self.idle_sprites = []

        self.idle_sprites.append(pygame.image.load('enemy_sprites/idle/WIZARD_IDLE_0.png'))
        self.idle_sprites.append(pygame.image.load('enemy_sprites/idle/WIZARD_IDLE_1.png'))
        self.idle_sprites.append(pygame.image.load('enemy_sprites/idle/WIZARD_IDLE_2.png'))
        self.idle_sprites.append(pygame.image.load('enemy_sprites/idle/WIZARD_IDLE_3.png'))

        self.walk_sprites = []

        self.walk_sprites.append(pygame.image.load('enemy_sprites/walk/WIZARD_WALK_0.png'))
        self.walk_sprites.append(pygame.image.load('enemy_sprites/walk/WIZARD_WALK_1.png'))
        self.walk_sprites.append(pygame.image.load('enemy_sprites/walk/WIZARD_WALK_2.png'))
        self.walk_sprites.append(pygame.image.load('enemy_sprites/walk/WIZARD_WALK_3.png'))

        self.attack_sprites = []

        self.attack_sprites.append(pygame.image.load('enemy_sprites/attack/WIZARD_ATTACK_0.png'))
        self.attack_sprites.append(pygame.image.load('enemy_sprites/attack/WIZARD_ATTACK_1.png'))
        self.attack_sprites.append(pygame.image.load('enemy_sprites/attack/WIZARD_ATTACK_2.png'))
        self.attack_sprites.append(pygame.image.load('enemy_sprites/attack/WIZARD_ATTACK_3.png'))

        self.current_walk_sprite = 0
        self.walk_image = self.walk_sprites[self.current_walk_sprite]


        self.current_idle_sprite = 0
        self.idle_image = self.idle_sprites[self.current_idle_sprite]


    def walk_animation(self):
        self.current_walk_sprite += 0.05
        if self.current_walk_sprite >= len(self.walk_sprites):
            self.current_walk_sprite = 0
        self.walk_image = self.walk_sprites[int(self.current_walk_sprite)]
        self.walk_image = pygame.transform.scale(self.walk_image, (self.width, self.height))

    def idle_animation(self):
        self.current_idle_sprite += 0.05
        if self.current_idle_sprite >= len(self.idle_sprites):
            self.current_idle_sprite = 0
        self.idle_image = self.idle_sprites[int(self.current_idle_sprite)]
        self.idle_image = pygame.transform.scale(self.idle_image, (self.width, self.height))
        

    def move(self, eventManager, renderer, delta_time, player):
        dx = 0
        dy = 0
        if self.direction == 'left':
            dx -= self.vel * delta_time
        elif self.direction == 'right':
            dx += self.vel * delta_time



        if ((player.new_x - (self.x + dx) < 200 and player.new_x > self.x) or (self.x + dx - player.new_x < 200 and player.new_x < self.x)) and player.new_y - self.y < 200 and player.new_y - self.y > -200:
            if player.new_x > self.x:
                self.direction = 'right'
            elif player.new_x < self.x:
                self.direction = 'left'
            dx = 0
            self.attack = True



            self.idle = True
            self.walk = False
            self.attack_player(player, renderer)

        super().move(eventManager, renderer, delta_time, dx, dy)


        newHitboxX = pygame.Rect(self.x, self.y, self.width, self.height)


        for hitbox in eventManager.enemy_hitboxes:
            if hitbox.colliderect(newHitboxX):
                self.change_direction()
                break

        if self.x < 0:
            self.change_direction()
        if self.x + self.width > 2200:
            self.change_direction()



    def attack_player(self, player, renderer):
        if self.attack:
            pygame.draw.line(renderer.win, (0, 0, 0), (player.x, player.y), (self.x, self.y), 5)
        




    def change_direction(self):
        if self.direction == 'left':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'left'



    def show(self, renderer):
        offsetRect = pygame.Rect(self.x - renderer.scroll_x, self.y - renderer.scroll_y, self.width, self.height)
        # pygame.draw.rect(renderer.win, (255, 0, 0), offsetRect)
        if self.walk:
            if self.direction == 'left':
                self.walk_image = pygame.transform.flip(self.walk_image, True, False)
            if self.direction == 'right':
                self.walk_image = pygame.transform.flip(self.walk_image, False, False)
        
            renderer.win.blit(self.walk_image, offsetRect)

        if self.idle:
            if self.direction == 'left':
                self.idle_image = pygame.transform.flip(self.idle_image, True, False)
            if self.direction == 'right':
                self.idle_image = pygame.transform.flip(self.idle_image, False, False)
        
            renderer.win.blit(self.idle_image, offsetRect)
            self.idle = False
<<<<<<< HEAD
            self.walk = True
=======
            self.walk = True
>>>>>>> aae776e60b0a9864550db068fe03597c5edad5d7
