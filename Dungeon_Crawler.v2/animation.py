import pygame


def select_animations_list(sprite_name):
    if sprite_name == "player":
        return animations_player


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('assets/' + sprite_name + '.png')
        self.current_image = 0  # commencer l'animation à l'image 0
        self.images = []
        self.name_list_animations = None
        self.animation = False
        self.animation_dict = select_animations_list(sprite_name)
        self.move_type = None
        self.c = 0

    def start_animation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self, sprite_name, move_type, loop=False):

        # verifier si l'animation est active
        if self.animation:

            # prendre la bonne liste
            self.name_list_animations = f'{sprite_name}_{move_type}'

            # mettre les images dans la liste
            self.images = self.animation_dict.get(self.name_list_animations)

            # passer à l'image suivante
            self.current_image += 1

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation à 0
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:

                    # desactiver l'animation
                    self.animation = False

            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]

    def timer_animation(self):
        self.c += 1

        if self.c == 5:
            self.c = 0

        return self.c


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name, frame_beginner, last_frame):
    # charger les images de ce sprite dans le dossier correspondant
    images = []

    # recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(frame_beginner, last_frame + 1):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# player -> [...player1.png, ...player2.png]
animations_player = {
    'player_idle': load_animation_images('player', 50, 56),
    'player_walk': load_animation_images('player', 4, 7),
    'player_run': load_animation_images('player', 8, 15),
    'player-kneel': load_animation_images('player', 16, 22),
    'player_jump': load_animation_images('player', 23, 30),
    'player_disappear': load_animation_images('player', 31, 33),
    'player_die': load_animation_images('player', 34, 41),
    'player_attack': load_animation_images('player', 42, 50)

}
