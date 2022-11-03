
import pygame
import random


class Game():

    def __init__(self, player, pokemons):
        self.player = player
        self.pokemons = pokemons
        self.font_text_title = pygame.font.SysFont("calibri", 50)


    def update(self):
        pass

    def draw(self):

        white = (255,255,255)

        pokemon_text_title = self.font_text_title.render("Hra Pokémon", True, white)
        pokemon_text_title_rect = pokemon_text_title.get_rect()
        pokemon_text_title_rect.centerx = width // 2
        pokemon_text_title_rect.top = 25
        screen.blit(pokemon_text_title, pokemon_text_title_rect)

    def pause():
        pass

    def reset():
        pass

class Playr(pygame.sprite.Sprite):

    def __init__(self, x, y, name = ("playr1")):
        super().__init__()
        self.image = pygame.image.load("Img/Pikachu.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.bottom = height -20
        self.rect.left = 20
        self.speed = 3
        self.x = x
        self.y = y
        self.name = name
        self.healt = 100
        self.dmg = random.randint(5,20)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.speed

    def levels():
        pass

    def reset():
        pass


class Pokemon(pygame.sprite.Sprite):

    def __init__(self, x, y, image, type):
        super().__init__()
        self.image = pygame.transform.scale(image,(70,70))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.type = type
        self.x = x
        self.y = y
        self.healt = 100
        self.dmg = random.randint(5,20)


    def attacks(self, x, y,):

        self.attack = pygame.image.load("Img/Attacks/attack.png")
        self.attack_rec = self.attack.get_rect()
        self.attack_rec.topleft = (x + 100 ,y + 100)

        attack_position = (x + 40, y + 64)

        if self.type == 0:
            fire_attack = pygame.image.load("Img/Attacks/fire.png")
            fire_attack_rec = fire_attack.get_rect()
            fire_attack_rec.topleft = attack_position
            attack_type = fire_attack
            attack_type_rec = fire_attack_rec
        elif self.type == 1:
            wather_attack = pygame.image.load("Img/Attacks/wather.png")
            wather_attack_rec = wather_attack.get_rect()
            wather_attack_rec.topleft = attack_position
            attack_type = wather_attack
            attack_type_rec = wather_attack_rec
        elif self.type == 2:
            flight_attack = pygame.image.load("Img/Attacks/flight.png")
            flight_attack_rec = flight_attack.get_rect()
            flight_attack_rec.topleft = attack_position
            attack_type = flight_attack
            attack_type_rec = flight_attack_rec
        elif self.type == 3:
            lightn_attack = pygame.image.load("Img/Attacks/lightn.png")
            lightn_attack_rec = lightn_attack.get_rect()
            lightn_attack_rec.topleft = attack_position
            attack_type = lightn_attack
            attack_type_rec = lightn_attack_rec

        return x, y, self.attack, self.attack_rec, attack_type, attack_type_rec

    def update(self):
        self.attacks(self.x, self.y)


pygame.init()

width = 1600
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pokemon")

fps = 60
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

random_height = random.randint(100,height)
random_width = random.randint(100,height)

pokemon_group = pygame.sprite.Group()
arcanine = Pokemon(random_width, random_height, pygame.image.load("Img/Arcanine.png"),0)
pokemon_group.add(arcanine)

playr_group = pygame.sprite.Group()
playr = Playr(100, height // 2)
playr_group.add(playr)

my_game = Game(playr,pokemon_group)

lets_continue = True

while lets_continue:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    
    screen.fill((0,0,0))

    pygame.draw.line(screen, white, (0, 100), (width, 100))

    pokemon_group.draw(screen)
    pokemon_group.update()
    playr_group.draw(screen)
    playr_group.update()
    my_game.draw()
    my_game.update()

    pygame.display.update()

    clock.tick(fps)

pygame.quit()