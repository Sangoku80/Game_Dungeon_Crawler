import pygame
import pytmx
import pyscroll
from player import Player


class Game:

    def __init__(self):

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dungeon_Crawler")

        # chager la carte (tmx)
        self.tmx_data = pytmx.util_pygame.load_pygame('Assets/maps/map_level_1_1.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 5

        # generer un joueur
        player_position = self.tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # definir une liste qui va stocker les rectangles de collisions
        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:

            self.player.speed += 2

            if pressed[pygame.K_UP]:
                self.player.move_up("run")

            elif pressed[pygame.K_DOWN]:
                self.player.move_down("run")

            elif pressed[pygame.K_LEFT]:
                self.player.move_left("run")

            elif pressed[pygame.K_RIGHT]:
                self.player.move_right("run")

        else:

            if pressed[pygame.K_UP]:
                self.player.move_up("walk")

            elif pressed[pygame.K_DOWN]:
                self.player.move_down("walk")

            elif pressed[pygame.K_LEFT]:
                self.player.move_left("walk")

            elif pressed[pygame.K_RIGHT]:
                self.player.move_right("walk")

            else:
                self.player.move_idle()

    def update(self):
        self.group.update()

        # verification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.speed = 3.2
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)

            # méthode pour ralentir l'animation des sprites
            if self.player.timer_animation() == 0:
                self.player.update_animation(self.player.move_type)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(30)

        pygame.quit()
