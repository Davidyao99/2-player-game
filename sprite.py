from setup import *
import pygame as pg

vec = pg.math.Vector2


class Player1(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.extra_jump = False

    def jump(self, player):
        #jump only if standing on a platform
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms,False) or pg.sprite.collide_rect(self, player)
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
            self.extra_jump = True
        elif self.extra_jump:
            self.vel.y = -PLAYER_JUMP
            self.extra_jump = False
        
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            
        if keys[pg.K_DOWN]:
            self.vel.y = 20



        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        

        self.rect.midbottom = self.pos
        
    def kill(self):
        self.kill
        
class Player2(pg.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, HEIGHT / 2)
        self.pos = vec(WIDTH / 4,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.extra_jump = False

    def jump(self, player):
        #jump only if standing on a platform
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms,False) or pg.sprite.collide_rect(self, player)
        
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
            self.extra_jump = True
        elif self.extra_jump:
            self.vel.y = -PLAYER_JUMP
            self.extra_jump = False
        
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
            
        if keys[pg.K_s]:
            self.vel.y = 20



        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        

        self.rect.midbottom = self.pos
        
    def kill(self):
        self.kill()



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

