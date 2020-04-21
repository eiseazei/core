#!/usr/bin/python3.7

import pygame
import pygame.freetype

import vector
import score
import wall

class Pong:
    """A class that implement ping-pong game."""
    # frames limit value 
    FPS = 25
    
    # window dimensions
    WIDTH  = 600
    HEIGHT = 600
    WINSIZE = (WIDTH, HEIGHT)
    
    # object's colors 
    BGCOLOR = (0, 0, 0)
    PLCOLOR = (0, 255, 0)
    BACOLOR = (255, 255, 255)
    ENCOLOR = (255, 0, 0)
    
    def __init__(self):
        """Initialize class instance."""
        self.screen = pygame.display.set_mode(Pong.WINSIZE)
        self.label  = pygame.freetype.SysFont('Sans', 35)

        self.lw = wall.Wall(vector.Vector(0),
                            pygame.Rect(-20, 0, 20, Pong.HEIGHT),
                            Pong.BGCOLOR)

        self.rw = wall.Wall(vector.Vector(180),
                            pygame.Rect(Pong.WIDTH, 0, 20, Pong.HEIGHT),
                            Pong.BGCOLOR)

        self.tw = wall.Wall(vector.Vector(270),
                            pygame.Rect(0, 0, Pong.WIDTH, 20),
                            Pong.BGCOLOR)

        self.bw = wall.Wall(vector.Vector(90),
                            pygame.Rect(0, Pong.HEIGHT - 20, Pong.WIDTH, 20),
                            Pong.BGCOLOR)

        self.pl = wall.Player(vector.Vector(90),
                              pygame.Rect(Pong.WIDTH / 2 - 80 / 2, Pong.HEIGHT - 20, 80, 20),
                              Pong.PLCOLOR)

        self.en = wall.Player(vector.Vector(270),
                             pygame.Rect(Pong.WIDTH / 2 - 80 / 2, 0, 80, 20),
                             Pong.ENCOLOR)

        self.ba = wall.Ball(vector.Vector(270, 10),
                            pygame.Rect(Pong.WIDTH / 2 - 20 / 2, Pong.HEIGHT / 2 - 20 /2, 20, 20),
                            Pong.BACOLOR)

        self.sc = score.Score()

        self.message = ''

        self.make_ready()

    def make_ready(self) -> None:
        """Make preparation before game round."""
        self.ba.reset_position()
        self.ba.randomize_angle()
        self.ba.stop()

        self.pl.reset_position()
        self.en.reset_position()

        self.playing = False

        if self.sc.is_over():
            self.message = self.sc.over_decision()
        else:
            self.message = self.sc.status()
            pygame.time.set_timer(pygame.USEREVENT, 3000)

    def process_k_left(self) -> None:
        """Handle users left button press."""
        if not self.pl.rectangle.colliderect(self.lw.rectangle):
            self.pl.move_left()
    
    def process_k_right(self) -> None:
        """Handle users right button press."""
        if not self.pl.rectangle.colliderect(self.rw.rectangle):
            self.pl.move_right()

    def events(self) -> None:
        """Process keyboard and user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit('bye!')
            elif event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 0)
                
                self.playing = True
                self.ba.start()

            elif self.playing and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.process_k_left()

                elif event.key == pygame.K_RIGHT:
                    self.process_k_right()
            else:
                pass

    def update(self) -> None:
        """Update ball position, bounce and score."""
        self.ba.update()

        # update enemy
        if self.en.rectangle.left > self.ba.rectangle.centerx:
            if not self.en.rectangle.colliderect(self.lw.rectangle):
                self.en.move_left()
        
        if self.en.rectangle.right < self.ba.rectangle.centerx:
            if not self.en.rectangle.colliderect(self.lw.rectangle):
                self.en.move_right()

        # ball bounce
        if self.ba.rectangle.colliderect(self.pl.rectangle):
            self.ba.bounce(self.pl.vector)
            self.ba.vector.length += 1
            print(self.ba.vector.length)

        elif self.ba.rectangle.colliderect(self.en.rectangle):    
            self.ba.bounce(self.en.vector)

        elif self.ba.rectangle.colliderect(self.lw.rectangle):
            self.ba.bounce(self.lw.vector)

        elif self.ba.rectangle.colliderect(self.rw.rectangle):
            self.ba.bounce(self.rw.vector)

        # player win
        elif self.ba.rectangle.colliderect(self.tw.rectangle):
            pygame.time.delay(2000)
            self.sc.player_point()
            self.make_ready()

        # enemy win
        elif self.ba.rectangle.colliderect(self.bw.rectangle):
            pygame.time.delay(2000)
            self.sc.enemy_point()
            self.make_ready()

    def render(self) -> None:
        """Render game objects."""
        self.screen.fill(Pong.BGCOLOR)

        pygame.draw.rect(self.screen, self.pl.color, self.pl.rectangle)
        pygame.draw.rect(self.screen, self.en.color, self.en.rectangle)
        pygame.draw.rect(self.screen, self.ba.color, self.ba.rectangle)

        if not self.playing:
            x = (Pong.WIDTH / 2) - (len(self.message) * 8)
            y = 280
            self.label.render_to(self.screen,
                                 (x, y),
                                 self.message,
                                 Pong.BACOLOR,
                                 Pong.BGCOLOR)

        pygame.display.update()