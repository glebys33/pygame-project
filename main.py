import os
import sys
import time

import pygame

pygame.init()
pygame.display.set_caption('Игра')
size = WIDTH, HEIGHT = 920, 580
screen = pygame.display.set_mode(size)
t = time.time()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Mouse(pygame.sprite.Sprite):
    image = load_image("cursor.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Background(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('menu4.png'), (WIDTH, HEIGHT))
    image2 = pygame.transform.scale(load_image('menu4_1.png'), (WIDTH, HEIGHT))

    def __init__(self, group):
        super().__init__(group)
        self.image = Background.image1
        self.rect = self.image.get_rect()

    def update(self):
        global t
        if (time.time() - t) % 4 > 1:
            self.image = Background.image2
        elif (time.time() - t) % 4 > 2:
            pass
        elif (time.time() - t) % 4 > 3:
            pass
        else:
            self.image = Background.image1


class StartButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('start1.png'), (WIDTH * 0.33, HEIGHT * 0.125))
    image2 = pygame.transform.scale(load_image('start2.png'), (WIDTH * 0.33, HEIGHT * 0.125))

    def __init__(self, group, a=0):
        super().__init__(group)
        if a == 0:
            self.image = StartButton.image1
        elif a == 1:
            self.image = StartButton.image2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.25
        self.button = pygame.Rect(self.rect)

    def startgame(self):
        for i in fon_sprites:
            fon_sprites.remove(i)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = StartButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = StartButton.image1
        else:
            self.startgame()


class StatisticsButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('statistics1.png'), (WIDTH * 0.33, HEIGHT * 0.125))
    image2 = pygame.transform.scale(load_image('statistics2.png'), (WIDTH * 0.33, HEIGHT * 0.125))

    def __init__(self, group, a=0):
        super().__init__(group)
        if a == 0:
            self.image = StatisticsButton.image1
        elif a == 1:
            self.image = StatisticsButton.image2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.4
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = StatisticsButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = StatisticsButton.image1
        elif self in fon_sprites:
            pass


class SettingsButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('settings1.png'), (WIDTH * 0.33, HEIGHT * 0.125))
    image2 = pygame.transform.scale(load_image('settings2.png'), (WIDTH * 0.33, HEIGHT * 0.125))

    def __init__(self, group, a=0):
        super().__init__(group)
        if a == 0:
            self.image = SettingsButton.image1
        elif a == 1:
            self.image = SettingsButton.image2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.55
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = SettingsButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = SettingsButton.image1
        elif self in fon_sprites:
            pass


class QuitButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('quit1.png'), (WIDTH * 0.33, HEIGHT * 0.125))
    image2 = pygame.transform.scale(load_image('quit2.png'), (WIDTH * 0.33, HEIGHT * 0.125))

    def __init__(self, group, a=0):
        super().__init__(group)
        if a == 0:
            self.image = QuitButton.image1
        elif a == 1:
            self.image = QuitButton.image2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.7
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = QuitButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and self in fon_sprites:
            self.image = QuitButton.image1
        elif self in fon_sprites:
            return False
        return True


if __name__ == '__main__':
    fon_sprites = pygame.sprite.Group()
    mouse_sprite = pygame.sprite.Group()
    background = Background(fon_sprites)
    mouse = Mouse(mouse_sprite)
    start = StartButton(fon_sprites)
    statisticsmenu = StatisticsButton(fon_sprites)
    settings = SettingsButton(fon_sprites)
    quit = QuitButton(fon_sprites)
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse.rect.x, mouse.rect.y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                start.mousedown()
                settings.mousedown()
                statisticsmenu.mousedown()
                quit.mousedown()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.pos
                start.mouseup()
                settings.mouseup()
                statisticsmenu.mouseup()
                running = quit.mouseup()
        fon_sprites.draw(screen)
        fon_sprites.update()
        if pygame.mouse.get_focused():
            mouse_sprite.draw(screen)
            mouse_sprite.update()
        pygame.display.flip()
    pygame.quit()