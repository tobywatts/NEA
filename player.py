import pygame

from settings import *


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.new_x = 0
        self.new_y = 0
        self.width = 40
        self.height = 70
        self.vel = 350
        self.jump_vel = 0
        self.jump_height = 725
        self.health = 100
        self.gravity = 1500
        self.jump = False
        self.onGround = True
        self.player_img = pygame.image.load('player.png')
<<<<<<< HEAD
        self.shooting = False

        self.bullet_img = pygame.image.load('player_sprites/bullet_img.png')
        self.bullets_left = []
        self.bullets_right = []
        self.bullet_rects = []
        self.bullet_vel = 500


        self.ak = pygame.image.load('player_sprites/ak.png')



        self.ak = pygame.transform.rotate (self.ak, -45)
        self.gun_pos = (self.x + 20, self.y + 20)
        
        self.shoot = False
=======

        self.guns = []
        self.gun_sprites = pygame.image.load('player_sprites/ak.png')
        self.guns.append(self.gun_sprites.subsurface(0, 0, 32, 32))
        self.guns.append(self.gun_sprites.subsurface(32, 0, 32, 32))
        self.guns.append(self.gun_sprites.subsurface(64, 0, 32, 32))
        self.guns.append(self.gun_sprites.subsurface(96, 0, 32, 32))
        self.ak = self.gun_sprites.subsurface(64, 0, 32, 32)
>>>>>>> aae776e60b0a9864550db068fe03597c5edad5d7


        self.crosshair = pygame.image.load('crosshair.png')
        self.crosshair_rect = self.crosshair.get_rect()
        self.mouse_pos = pygame.mouse.get_pos()

        self.direction = 'left'

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def draw(self, renderer, delta_time):
        
        self.mouse_pos = pygame.mouse.get_pos()
        self.crosshair = pygame.transform.scale(self.crosshair, (32, 32))

        self.crosshair_rect.x = self.mouse_pos[0]
        self.crosshair_rect.y = self.mouse_pos[1]
        renderer.win.blit(self.crosshair, (self.mouse_pos[0] - 16, self.mouse_pos[1] - 16))


        new_player_img = pygame.transform.scale(self.player_img, (self.width, self.height))
        new_ak = pygame.transform.scale(self.ak, (50, 45))
        
        if self.direction == 'left':
            new_player_img = pygame.transform.flip(new_player_img, True, False)
            new_ak = pygame.transform.flip(new_ak, True, False)
            

        if self.direction == 'right':
            
            new_player_img = pygame.transform.flip(new_player_img, False, False)
            new_ak = pygame.transform.flip(new_ak, False, False)

        renderer.win.blit(new_player_img, (self.x - renderer.scroll_x, self.y - renderer.scroll_y))
<<<<<<< HEAD
        renderer.win.blit(new_ak, (self.x - renderer.scroll_x, self.y - renderer.scroll_y + 25))

        self.hitbox = pygame.Rect(self.x - renderer.scroll_x, self.y - renderer.scroll_y, self.width, self.height)

        if self.shoot == True:
            

            for bullet in self.bullets_right:

                if bullet.x > 2200:
                    self.bullets_right.remove(bullet)
                if bullet.x < 0:
                    self.bullets_right.remove(bullet)
                if bullet.y > 1200:
                    self.bullets_right.remove(bullet)
                if bullet.y < 0:
                    self.bullets_right.remove(bullet)
                    
                renderer.win.blit(self.bullet_img, bullet)
                bullet.x += self.bullet_vel * delta_time

                




            for bullet in self.bullets_left:

                if bullet.x > 2200:
                    self.bullets_left.remove(bullet)
                if bullet.x < 0:
                    self.bullets_left.remove(bullet)
                if bullet.y > 1200:
                    self.bullets_left.remove(bullet)
                if bullet.y < 0:
                    self.bullets_left.remove(bullet)
                    
                renderer.win.blit(self.bullet_img, bullet)
                
                bullet.x -= self.bullet_vel * delta_time
                
                self.shoot = False



    def show_bullet(self, renderer):
        if self.direction == 'right':
            self.gun_pos = (self.new_x + 50, self.new_y + 45)
            self.shoot = True


            if self.shoot == True:
                new_bullet = pygame.Rect(self.gun_pos[0] - renderer.scroll_x, self.gun_pos[1] - renderer.scroll_y, 10, 10)
                new_bullet_rect = pygame.Rect(self.gun_pos[0] - renderer.scroll_x, self.gun_pos[1] - renderer.scroll_y, 10, 10)
                if new_bullet not in self.bullets_left:
                    if self.direction == 'left':
                        self.bullets_left.append(new_bullet)
                        self.bullet_rects.append(new_bullet_rect)

                if new_bullet not in self.bullets_right:
                    if self.direction == 'right':
                        self.bullets_right.append(new_bullet)
                        self.bullet_rects.append(new_bullet_rect)

        if self.direction == 'left':
            self.gun_pos = (self.new_x - 10, self.new_y + 45)
            self.shoot = True
=======

        self.hitbox = pygame.Rect(self.x - renderer.scroll_x, self.y - renderer.scroll_y, self.width, self.height)

        # self.ak = pygame.transform.rotate (self.ak, -45)
        self.ak = pygame.transform.scale(self.ak, (32, 32))


        renderer.win.blit(self.ak, (self.x - renderer.scroll_x, self.y - renderer.scroll_y + 25))


        # pygame.draw.rect(renderer.win, (255, 0, 0), self.hitbox, 2)
>>>>>>> aae776e60b0a9864550db068fe03597c5edad5d7


    def key_events(self, newPosition, delta_time):
        keys = pygame.key.get_pressed()

        # moving
        if keys[pygame.K_a]:
            newPosition.x -= self.vel * delta_time
            if newPosition.x < 0:
                newPosition.x = 0
            self.direction = 'left'


        if keys[pygame.K_d]:
            newPosition.x += self.vel * delta_time
            if newPosition.x + self.width > 2200:
                newPosition.x = 2200 - self.width
            self.direction = 'right'

        


        # print(newPosition.x, newPosition.y)

        if self.onGround and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            # jump
            self.jump_vel = -self.jump_height
            self.onGround = False

            

    def move(self, eventManager, renderer, delta_time, dx=0, dy=0):
        newPosition = pygame.Vector2(self.x+dx, self.y+dy)

        if type(self) == Player:
            self.key_events(newPosition, delta_time)

        
        if not self.onGround:
            self.jump_vel += self.gravity * delta_time 
            self.jump_vel = min(1000, self.jump_vel)
        newPosition.y += self.jump_vel * delta_time
        
        newHitboxX = pygame.Rect(newPosition.x, self.y, self.width, self.height)
        newHitboxY = pygame.Rect(self.x, newPosition.y, self.width, self.height)

        # collision
        canMoveX = True
        for hitbox in eventManager.hitboxes:
            if hitbox.colliderect(newHitboxX):
                canMoveX = False
                break
        if canMoveX:
            self.x = newPosition.x

        else:
            # stops enemies from falling off the sides 
            if type(self) != Player:
                self.change_direction()
                return
        
        canMoveY = True
        for hitbox in eventManager.hitboxes:
            if hitbox.colliderect(newHitboxY):
                if newPosition.y < hitbox.y:
                    self.y = hitbox.y - self.height
                    self.onGround = True  
                    self.jump_vel = 0
                canMoveY = False
                break

        if canMoveY:
            self.onGround = False
            self.y = newPosition.y

        self.new_x = newPosition.x
        self.new_y = newPosition.y



        if type(self) == Player:
            # camera
            renderer.scroll_x = self.x - 400
            renderer.scroll_y = self.y - 320

            renderer.scroll_x = max(0, renderer.scroll_x)
            renderer.scroll_x = min(renderer.scroll_x, 1400)
            renderer.scroll_y = max(0, renderer.scroll_y)
            renderer.scroll_y = min(renderer.scroll_y, 640)

            # print(newPosition.x, newPosition.y)