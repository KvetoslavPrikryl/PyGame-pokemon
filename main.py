import pygame
import random

pygame.init()

# Display
width = 1500
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pokémon")

# Settings
fps = 60
distance = 10
clock = pygame.time.Clock()

# IMG

# Arcanine IMG
arcanine_img = pygame.image.load("Img/Arcanine.png")
arcanine_img_rect = arcanine_img.get_rect()
arcanine_img_rect.center = (width // 2, height // 2)

minigame_arcanine = pygame.image.load("Img/Arcanine.png")
minigame_arcanine = pygame.transform.scale(minigame_arcanine, (120, 120))
minigame_arcanine_rec = minigame_arcanine.get_rect()
minigame_arcanine_rec.center = (width - 150, height // 2) 

# Arcanine atributs
arcanine_start_live = 100
arcanine_live = arcanine_start_live

# Attack Arcanine
attack_arcanine = pygame.image.load("Img/Attacks/fire.png")
attack_arcanine = pygame.transform.scale(attack_arcanine, (50,50))
attack_arcanine_rec = attack_arcanine.get_rect()
attack_arcanine_rec.center = (width - 160, height - 60)

#--------------------------------------------------------------------------------------------------#
# Hero Img
hero_img = pygame.image.load("Img/Pikachu.png")
hero_img = pygame.transform.scale(hero_img, (90, 90))
hero_img_rect = hero_img.get_rect()
hero_img_rect.center = (width // 2, 700)

minigame_hero = pygame.image.load("Img/Pikachu.png")
minigame_hero = pygame.transform.scale(minigame_hero, (90, 90))
minigame_hero_rec = minigame_hero.get_rect()
minigame_hero_rec.center = (150, height // 2)

# Hero atributs
hero_start_live = 100
hero_live = hero_start_live

# Atack Hero
attack_hero = pygame.image.load("Img/Attacks/lightn.png")
attack_hero = pygame.transform.scale(attack_hero, (50,50))
attack_hero_rec = attack_hero.get_rect()
attack_hero_rec.center = (160, height - 60)
#---------------------------------------------------------------------------------------------------#
# Arena
arena_img = pygame.image.load("Img/Arena.png")
arena_img = pygame.transform.scale(arena_img, (width, height))
arena_img_rec = arena_img.get_rect()
arena_img_rec.topleft = (0,0)

# Color
white = (255, 255, 255)

# Font
font_text = pygame.font.SysFont("calibri", 30)
# Text
pokemon_text = font_text.render("Hra Pokémon", True, white)
pokemon_text_rect = pokemon_text.get_rect()
pokemon_text_rect.centerx = width // 2
pokemon_text_rect.centery = 50 // 2
text_arcanine_live = font_text.render(f"Životy: {arcanine_live}", True, white)
text_arcanine_live_rec = text_arcanine_live.get_rect()
text_arcanine_live_rec.center = (width - 100, 100)
text_hero_live = font_text.render(f"Životy: {hero_live}", True, white)
text_hero_live_rec = text_hero_live.get_rect()
text_hero_live_rec.center = (100, 100)

# Main cycle
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and hero_img_rect.top > 50:
        hero_img_rect.y -= distance
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and hero_img_rect.bottom < height:
        hero_img_rect.y += distance
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and hero_img_rect.left > 0:
        hero_img_rect.x -= distance
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and hero_img_rect.right < width:
        hero_img_rect.x += distance

    # Collision
    if hero_img_rect.colliderect(arcanine_img_rect):
        arcanine_img_rect.centerx = random.randint(0 + 36, width - 36)
        arcanine_img_rect.centery = random.randint(50 + 36, height - 36)

        arcanine_live = arcanine_start_live
        hero_live = hero_start_live

        minigame = True

        while minigame:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    minigame = False
                    lets_continue = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x = event.pos[0]
                    click_y = event.pos[1]

                    if attack_hero_rec.collidepoint(click_x, click_y):
                        arcanine_live -= random.randint(5,20)
                        if arcanine_live <= 0:
                            minigame = False

                    hero_live -= random.randint(5,20)
                    if hero_live <= 0 :
                        minigame = False
                    
                    
            text_arcanine_live = font_text.render(f"Životy: {arcanine_live}", True, white)
            text_hero_live = font_text.render(f"Životy: {hero_live}", True, white)
            

            screen.fill((0, 0, 0))

            pygame.draw.line(screen, white, (0, 50), (width, 50))

            screen.blit(arena_img, arena_img_rec)
            screen.blit(minigame_arcanine, minigame_arcanine_rec)
            screen.blit(minigame_hero, minigame_hero_rec)
            screen.blit(pokemon_text, pokemon_text_rect)
            screen.blit(attack_arcanine, attack_arcanine_rec)
            screen.blit(attack_hero, attack_hero_rec)
            screen.blit(text_arcanine_live, text_arcanine_live_rec)
            screen.blit(text_hero_live, text_hero_live_rec)

            pygame.display.update()
            clock.tick(fps)

    screen.fill((0, 0, 0))

    # Shapes
    pygame.draw.line(screen, white, (0, 50), (width, 50))

    # BLIT
    screen.blit(arcanine_img, arcanine_img_rect)
    screen.blit(hero_img, hero_img_rect)
    screen.blit(pokemon_text, pokemon_text_rect)

    # Update display
    pygame.display.update()

    # FPS
    clock.tick(fps)

pygame.quit()
