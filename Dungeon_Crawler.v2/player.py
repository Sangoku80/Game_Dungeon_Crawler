import animation
import pygame


class Player(animation.AnimateSprite):

    def __init__(self, x, y):
        super().__init__('player')
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 3
        self.animation_move_right = []
        self.old_position = self.position.copy()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)

    def move_right(self, run_or_walk):
        self.position[0] += self.speed
        self.start_animation()
        self.move_type = run_or_walk

    def move_left(self, run_or_walk):
        self.position[0] -= self.speed
        self.start_animation()
        self.move_type = run_or_walk

    def move_up(self, run_or_walk):
        self.position[1] -= self.speed
        self.start_animation()
        self.move_type = run_or_walk

    def move_down(self, run_or_walk):
        self.position[1] += self.speed
        self.start_animation()
        self.move_type = run_or_walk

    def move_idle(self):
        self.start_animation()
        self.move_type = "idle"

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def save_location(self):
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def update_animation(self, move_type):
        self.animate('player', move_type)
