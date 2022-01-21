import os
import sys
import time

import pygame

pygame.init()
with open(os.path.join('data', 'settings.txt')) as file:
    for row in file:
        if (s:=row.split())[0] == 'WIDTH':
            WIDTH = int(s[1])
        elif s[0] == 'HEIGHT':
            HEIGHT = int(s[1])
        elif s[0] == 'volume':
            volume = float(s[1])
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.load('data/Menu.mp3')
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

    def update_sprite(self):
        self.image = Mouse.image
        self.rect = self.image.get_rect()


class Background(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('menu4.png'), (WIDTH, HEIGHT))
    image2 = pygame.transform.scale(load_image('menu4_1.png'), (WIDTH, HEIGHT))

    def __init__(self, group):
        super().__init__(group)
        self.image = Background.image1
        self.rect = self.image.get_rect()
        self.scane = 'menu'

    def update(self):
        global t
        if (time.time() - t) % 2 > 1:
            self.image = Background.image2
        else:
            self.image = Background.image1

    def update_sprite(self):
        Background.image1 = pygame.transform.scale(load_image('menu4.png'), (WIDTH, HEIGHT))
        Background.image2 = pygame.transform.scale(load_image('menu4_1.png'), (WIDTH, HEIGHT))
        self.image = Background.image1
        self.rect = self.image.get_rect()


class StartButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('start1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
    image2 = pygame.transform.scale(load_image('start2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))

    def __init__(self, group):
        super().__init__(group)
        self.image = StartButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.25
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = StartButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = StartButton.image1
        elif background.scane == 'menu':
            self.startgame()

    def startgame(self):
        background.scane = 'game'

    def update_sprite(self):
        StartButton.image1 = pygame.transform.scale(load_image('start1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        StartButton.image2 = pygame.transform.scale(load_image('start2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        self.image = StartButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.25
        self.button = pygame.Rect(self.rect)


class StatisticsButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('statistics1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
    image2 = pygame.transform.scale(load_image('statistics2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))

    def __init__(self, group):
        super().__init__(group)
        self.image = StatisticsButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.4
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = StatisticsButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = StatisticsButton.image1
        elif background.scane == 'menu':
            background.scane = 'statistics'

    def update_sprite(self):
        StatisticsButton.image1 = pygame.transform.scale(load_image('statistics1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        StatisticsButton.image2 = pygame.transform.scale(load_image('statistics2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        self.image = StatisticsButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.4
        self.button = pygame.Rect(self.rect)


class SettingsButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('settings1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
    image2 = pygame.transform.scale(load_image('settings2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))

    def __init__(self, group):
        super().__init__(group)
        self.image = SettingsButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.55
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = SettingsButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = SettingsButton.image1
        elif background.scane == 'menu':
            background.scane = 'settings'

    def update_sprite(self):
        SettingsButton.image1 = pygame.transform.scale(load_image('settings1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        SettingsButton.image2 = pygame.transform.scale(load_image('settings2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        self.image = SettingsButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.55
        self.button = pygame.Rect(self.rect)


class QuitButton(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('quit1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
    image2 = pygame.transform.scale(load_image('quit2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))

    def __init__(self, group):
        super().__init__(group)
        self.image = QuitButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.7
        self.button = pygame.Rect(self.rect)

    def mousedown(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = QuitButton.image2

    def mouseup(self):
        if not self.button.collidepoint(mouse_pos) and background.scane == 'menu':
            self.image = QuitButton.image1
        elif background.scane == 'menu':
            return False
        return True

    def update_sprite(self):
        QuitButton.image1 = pygame.transform.scale(load_image('quit1.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        QuitButton.image2 = pygame.transform.scale(load_image('quit2.png'), (int(WIDTH * 0.33), int(HEIGHT * 0.125)))
        self.image = QuitButton.image1
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.7
        self.button = pygame.Rect(self.rect)


class CloseButton(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('close.png'), (int(WIDTH * 0.1), int(HEIGHT * 0.04)))

    def __init__(self, group):
        super().__init__(group)
        self.image = CloseButton.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.69
        self.rect.y = HEIGHT * 0.915
        self.button = pygame.Rect(self.rect)

    def mouseup(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'settings':
            background.scane = 'menu'

    def update_sprite(self):
        CloseButton.image = pygame.transform.scale(load_image('close.png'), (int(WIDTH * 0.1), int(HEIGHT * 0.04)))
        self.image = CloseButton.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.69
        self.rect.y = HEIGHT * 0.915
        self.button = pygame.Rect(self.rect)


class ApplyButton(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('apply.png'), (int(WIDTH * 0.1), int(HEIGHT * 0.04)))

    def __init__(self, group):
        super().__init__(group)
        self.image = ApplyButton.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.8
        self.rect.y = HEIGHT * 0.915
        self.button = pygame.Rect(self.rect)

    def mouseup(self):
        if self.button.collidepoint(mouse_pos) and background.scane == 'settings':
            background.scane = 'menu'
            global screen, WIDTH, HEIGHT
            WIDTH = 520
            HEIGHT = 720
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            update_all_sprites()

    def update_sprite(self):
        ApplyButton.image = pygame.transform.scale(load_image('apply.png'), (int(WIDTH * 0.1), int(HEIGHT * 0.04)))
        self.image = ApplyButton.image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.8
        self.rect.y = HEIGHT * 0.915
        self.button = pygame.Rect(self.rect)
        
   class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))


def update_all_sprites():
    background.update_sprite()
    mouse.update_sprite()
    start.update_sprite()
    statisticsmenu.update_sprite()
    settings.update_sprite()
    quit.update_sprite()
    apply.update_sprite()
    close.update_sprite()


if __name__ == '__main__':
    background_sprite = pygame.sprite.Group()
    menu_sprites = pygame.sprite.Group()
    settings_sprites = pygame.sprite.Group()
    game_sprites = pygame.sprite.Group()
    mouse_sprite = pygame.sprite.Group()
    background = Background(background_sprite)
    mouse = Mouse(mouse_sprite)
    start = StartButton(menu_sprites)
    statisticsmenu = StatisticsButton(menu_sprites)
    settings = SettingsButton(menu_sprites)
    quit = QuitButton(menu_sprites)
    apply = ApplyButton(settings_sprites)
    close = CloseButton(settings_sprites)
    pygame.mouse.set_visible(False)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill('black')
        clock.tick()
        pygame.display.set_caption(str(int(clock.get_fps())))
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
                close.mouseup()
                apply.mouseup()
        background_sprite.draw(screen)
        background_sprite.update()

        if background.scane == 'menu':
            menu_sprites.draw(screen)
            menu_sprites.update()
        elif background.scane == 'settings':
            settings_sprites.draw(screen)
            settings_sprites.update()

        if pygame.mouse.get_focused():
            mouse_sprite.draw(screen)
            mouse_sprite.update()
        pygame.display.flip()
    pygame.quit()
