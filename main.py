import pygame as pg
import random
from setup import *
from sprite import *

class Game:
    
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)


    def new(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player1 = Player1(self)
        self.all_sprites.add(self.player1)
        self.player2 = Player2(self)
        self.all_sprites.add(self.player2)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        self.run()

    def run(self):
        
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        #Game Loop - Update
        self.all_sprites.update()
        #check if player hits a platform - only if falling
        hits_platform = pg.sprite.spritecollide(self.player1, self.platforms, False)
        if hits_platform:
            self.player1.pos.y = hits_platform[0].rect.top + 1
            self.player1.vel.y = 0
        hits_players = pg.sprite.collide_rect(self.player1, self.player2)
        if hits_players:
            if self.player1.rect.right > self.player2.rect.left and self.player1.rect.right < self.player2.rect.right:
                self.player1.vel.x = -10
                self.player2.vel.x= 10
            elif self.player2.rect.right > self.player1.rect.left and self.player2.rect.right < self.player1.rect.right:
                self.player1.vel.x = 10
                self.player2.vel.x= -10
            if self.player1.rect.bottom > self.player2.rect.top and self.player1.rect.top < self.player2.rect.top:
                self.score_p1 += 1
                self.player1.pos.y = self.player2.rect.top
                self.player1.vel.y = -10
                self.player2.vel.y = 10
            elif self.player2.rect.bottom > self.player1.rect.top and self.player2.rect.top < self.player1.rect.top:
                    self.score_p2 += 1
                    self.player2.pos.y = self.player1.rect.top
                    self.player2.vel.y = 0
                    self.player2.vel.y = -10
                    self.player1.vel.y = 10
            
        if self.player2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top + 1
                self.player2.vel.y = 0
                


            
        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player2.jump(self.player1)
                if event.key == pg.K_UP:
                    self.player1.jump(self.player2)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score_p2) + " : " + str(self.score_p1), 22, WHITE, WIDTH / 2, 25)
        pg.display.flip()
        
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



g = Game()

while g.running:
    g.new()

pg.quit()
quit()
