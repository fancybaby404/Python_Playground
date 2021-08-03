import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # images
        self.player_index = 0
        self.player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        self.player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [self.player_walk_1, self.player_walk_2]

        # sfx
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

        self.image = self.player_walk[self.player_index]

        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.jumps = 1
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()

        # Keyboard Controls
        if self.jumps == 1:
            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.jump_sound.play()
                self.gravity = -20
                self.jumps = 0

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0
            self.jumps = 1

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type_of_obstacle):
        super().__init__()
        self.type_of_obstacle = type_of_obstacle
        self.animation_index = 0

        if self.type_of_obstacle.lower() == 'snail':
            # Snail
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        elif self.type_of_obstacle.lower() == 'fly':
            # Fly
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index > len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()


# | Functions
def display_score():
    start_time = round(pygame.time.get_ticks() / 1000 - end_time)
    score_surface = FONT3.render(f'Score: {start_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 50))

    # | Create Outline
    pygame.draw.rect(display, '#66B5CC', score_rectangle, 10)
    pygame.draw.rect(display, '#66B5CC', score_rectangle)

    # | Display Score
    display.blit(score_surface, score_rectangle)

    return start_time


def collision_sprite():
    global start_game_timer
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        start_game_timer = 0
        obstacle_group.empty()
        return False
    else:
        return True


# | Game Initializations
pygame.init()
display = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DinoRun')
clock = pygame.time.Clock()
score = 0
game_active = False
start_game_timer = 0
end_time = 0
bg_music = pygame.mixer.Sound('./audio/music.wav')
bg_music.set_volume(0.2)

bg_music.play(loops=-0)

sky_surface = pygame.image.load('./graphics/sora.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()

FONT = pygame.font.Font('./font/Pixeltype.ttf', 150)
FONT2 = pygame.font.Font('./font/Pixeltype.ttf', 75)
FONT3 = pygame.font.Font('./font/Pixeltype.ttf', 50)

# | Player Initialization
player = pygame.sprite.GroupSingle()
player.add(Player())

# | Obstacles Initialization
obstacle_group = pygame.sprite.Group()

# | Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 300)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 150)

# | Intro Screen Initializations
player_stand = pygame.image.load('./graphics/player/player_stand.png').convert_alpha()
# scale:
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))

title_surface = FONT.render('AstroRun', True, (0, 0, 0))
title_rectangle = title_surface.get_rect(center=(400, 80))

instruct_surface = FONT3.render('Press SPACE to start', True, (0, 0, 0))
instruct_rectangle = title_surface.get_rect(center=(420, 350))

while True:
    # ----------------------- START OF FOR EVENT LOOP ----------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Spawning Mechanism
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

        else:
            print(start_game_timer)
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                end_time = round(pygame.time.get_ticks() / 1000)
                if start_game_timer > 10:
                    game_active = True

    # --------------------- ---- END OF FOR EVENT LOOP ------------------------- #

    if game_active:
        # | Environment
        display.blit(sky_surface, (0, 0))
        display.blit(ground_surface, (0, 300))

        score = display_score()

        # | Player
        player.draw(display)
        player.update()

        # | Obstacles
        obstacle_group.draw(display)
        obstacle_group.update()

        # | Collision
        game_active = collision_sprite()

    else:
        start_game_timer += 0.1

        display.fill((64, 161, 191))

        # Title Text
        display.blit(title_surface, title_rectangle)

        # Instructions Text
        if score == 0:
            display.blit(instruct_surface, instruct_rectangle)

        # Score Text
        else:
            score_message = FONT3.render(f'Your score: {score}', False, (0, 0, 0))
            score_rect = score_message.get_rect(center=(400, 330))
            display.blit(score_message, score_rect)

        # Image
        display.blit(player_stand, player_stand_rect)

    pygame.display.update()
    clock.tick(60)
