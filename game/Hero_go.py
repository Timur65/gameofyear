import pygame
import pygame_menu
import pygame as pg
import time
import random
from random import randint
from pygame.transform import scale

pygame.init()
wh = 1000
wl = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fon = (50, 183, 108)
font = pg.font.Font(None, 50)
points = 0
x = 0
y = 0
xe = 975
ye = 975
ts = 0.05
step = 25
spawn_1 = [3, 5, 7, 9, 11, 13, 15, 17]
spawn_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]


def End():
    screen = pygame.display.set_mode((wl, wh), pygame.NOFRAME)
    pygame.display.set_caption("Hero's Adventure")
    Maps = ["background1-.jpg", "background2-.jpg", "background3-.jpg"]
    bg_2 = pygame.image.load(Maps[map])
    backg_2 = scale(bg_2, (wl, wh))
    font = pg.font.Font(None, 30)
    ps = fs = 0
    st1 = "Поздравляем, с завершением уровня!"
    st2 = str("Имя: " + hero_name.get_value())
    st3 = str("Сложность: " + difficulty.get_value()[0][0])
    st5 = str("Очки: " + str(points))
    ST = [st1, st2, st3, st5]
    sT = ''
    y = 270
    while True:
        screen.blit(backg_2, (0, 0))
        pygame.draw.rect(screen, WHITE, (250, 250, 550, 250))
        pygame.draw.rect(screen, BLACK, (250, 250, 550, 250), 4)
        for i in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 470 <= mouse_x <= 550 and 450 <= mouse_y <= 650:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    start_menu()

        for i in range(len(ST)):
            if fs == 1:
                continue
            for j in ST[i]:
                sT += j
                font = pg.font.Font(None, 30)
                q = font.render(sT, True, BLACK)
                time.sleep(0.05)
                screen.blit(q, (285, y))
                pygame.display.update()
            sT = ''
            y += 25
        fs = 1

        font = pg.font.Font(None, 50)
        fast = 'В меню'
        fast_1 = ''
        for i in fast:
            if ps == 1:
                screen.blit(gj, (285, 270))
                break
            fast_1 += i
            gj = font.render(fast_1, True, BLACK)
            time.sleep(0.05)
            screen.blit(gj, (470, 450))
            pygame.display.update()
        ps = 1


def game_first():
    screen = pygame.display.set_mode((wl, wh), pygame.NOFRAME)
    pygame.display.set_caption("Hero's Adventure")

    count = 0
    gf = 0
    sf = 0
    sf_1 = 0
    Maps = ["background1-.jpg", "background2-.jpg", "background3-.jpg"]

    bg_2 = pygame.image.load(Maps[map])
    backg_2 = scale(bg_2, (wl, wh))
    screen.blit(backg_2, (0, 0))
    pygame.display.update()
    time.sleep(0.7)

    image = scale(pygame.image.load("Ded.png"), (400, 600))
    image.set_colorkey(WHITE)
    screen.blit(image, (650, 100))
    pygame.display.update()
    time.sleep(0.7)

    pygame.draw.polygon(screen, WHITE,
                        [[600, 250], [250, 250], [250, 170], [700, 170], [700, 230], [770, 345], [685, 250]])
    pygame.draw.circle(screen, WHITE, (250, 210), 40)
    pygame.draw.circle(screen, WHITE, (700, 210), 40)
    pygame.display.update()
    time.sleep(0.7)
    ds = str("Приветствую, " + hero_name.get_value())
    ds_1 = ''
    font = pg.font.Font(None, 30)
    for i in ds:
        ds_1 += i
        go = font.render(ds_1, True, BLACK)
        time.sleep(ts)
        screen.blit(go, (370, 175))
        pygame.display.update()
    ds = "Мне необходимо ровно 25 лечебных трав"
    ds_1 = ''

    for i in ds:
        ds_1 += i
        gu = font.render(ds_1, True, BLACK)
        time.sleep(ts)
        screen.blit(gu, (260, 200))
        pygame.display.update()
    ds = "Можешь помочь мне в сборе?"
    ds_1 = ''

    for i in ds:
        ds_1 += i
        gg = font.render(ds_1, True, BLACK)
        time.sleep(ts)
        screen.blit(gg, (335, 225))
        pygame.display.update()
    time.sleep(0.1)

    bs = 0
    col = 1
    while bs == 0:
        if col == 1:
            pygame.draw.rect(screen, WHITE, (350, 600, 200, 50))
            pygame.draw.circle(screen, WHITE, (350, 625), 25)
            pygame.draw.circle(screen, WHITE, (550, 625), 25)
        else:
            pygame.draw.rect(screen, (193, 201, 205), (350, 600, 200, 50))
            pygame.draw.circle(screen, (193, 201, 205), (350, 625), 25)
            pygame.draw.circle(screen, (193, 201, 205), (550, 625), 25)

        font = pg.font.Font(None, 50)
        s1 = font.render("Конечно!", True, BLACK)
        screen.blit(s1, (370, 610))
        pygame.display.update()
        for i in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 350 <= mouse_x <= 550 and 600 <= mouse_y <= 650:
                col = 0
                if i.type == pygame.MOUSEBUTTONDOWN:
                    bs = 1
                    break
            else:
                col = 1
    rb = 0
    lb = 0
    run = 1
    ff = 0

    while run == 1:
        chance = [1, 6, 7, 8, 5, 9, 10, 2, 3, 4, 11, 12, 13] * 5
        random.shuffle(chance)
        screen.blit(backg_2, (0, 0))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                raise SystemExit("QUIT")

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 50 <= mouse_x <= 100 + 50 and 5 <= mouse_y <= 35:
                sf_1 = 1
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if sf == 0:
                        sf = 1
                    else:
                        sf = 0

            if 290 <= mouse_x <= 290 + 150 and 400 <= mouse_y <= 480:
                lb = 1
                if i.type == pygame.MOUSEBUTTONDOWN:
                    current = chance.pop()
                    ff = 1
                    count += current
                    gf = 0
            else:
                lb = 0

            if 610 <= mouse_x <= 760 and 400 <= mouse_y <= 480:
                rb = 1
                if i.type == pygame.MOUSEBUTTONDOWN:
                    run = 0
            else:
                rb = 0

        pygame.draw.rect(screen, WHITE, (250, 250, 550, 100))
        pygame.draw.rect(screen, BLACK, (250, 250, 550, 100), 4)
        font = pg.font.Font(None, 30)
        if ff == 1:
            fast = 'Было получено трав: %d' % current
            fast = str(fast)
            fast_1 = ''
            for i in fast:
                if gf == 1:
                    screen.blit(gj, (285, 270))
                    break
                fast_1 += i
                gj = font.render(fast_1, True, BLACK)
                time.sleep(ts)
                screen.blit(gj, (285, 270))
                pygame.display.update()
        g_12 = str('Сейчас у вас в наличии %d лечебных трав.' % count)
        g_13 = ''
        for i in g_12:
            if gf == 1:
                screen.blit(g_a, (285, 290))
                break
            g_13 += i
            g_a = font.render(g_13, True, BLACK)
            time.sleep(ts)
            screen.blit(g_a, (285, 290))
            pygame.display.update()

        g_2 = "Отправиться собирать травы?"
        g_3 = ''
        for i in g_2:
            if gf == 1:
                screen.blit(g2, (285, 310))
                break
            g_3 += i
            g2 = font.render(g_3, True, BLACK)
            time.sleep(ts)
            screen.blit(g2, (285, 310))
            pygame.display.update()

        gf = 1

        if lb == 0:
            pygame.draw.rect(screen, WHITE, (290, 400, 150, 80))
            pygame.draw.circle(screen, WHITE, (290, 440), 40)
            pygame.draw.circle(screen, WHITE, (440, 440), 40)

        else:
            pygame.draw.rect(screen, (193, 201, 205), (290, 400, 150, 80))
            pygame.draw.circle(screen, (193, 201, 205), (290, 440), 40)
            pygame.draw.circle(screen, (193, 201, 205), (440, 440), 40)

        if rb == 0:
            pygame.draw.rect(screen, WHITE, (610, 400, 150, 80))
            pygame.draw.circle(screen, WHITE, (610, 440), 40)
            pygame.draw.circle(screen, WHITE, (760, 440), 40)

        else:
            pygame.draw.rect(screen, (193, 201, 205), (610, 400, 150, 80))
            pygame.draw.circle(screen, (193, 201, 205), (610, 440), 40)
            pygame.draw.circle(screen, (193, 201, 205), (760, 440), 40)

        font = pg.font.Font(None, 50)
        s1 = font.render("Конечно!", True, BLACK)
        screen.blit(s1, (285, 425))

        font = pg.font.Font(None, 50)
        s1 = font.render("Закончить", True, BLACK)
        screen.blit(s1, (600, 425))

        font = pg.font.Font(None, 30)

        if sf == 1:
            pygame.draw.rect(screen, BLACK, (170, 10, 565, 80), 4)
            pygame.draw.rect(screen, WHITE, (174, 14, 557, 72))
            s2 = "Необходимо собрать ровно 25 лечебных трав: "
            s3 = "для получения большего количества очков лучше,"
            s4 = "не добрать пару штук, чем собрать чем больше нужно"
            s2_1 = font.render(s2, True, BLACK)
            s3_1 = font.render(s3, True, BLACK)
            s4_1 = font.render(s4, True, BLACK)
            screen.blit(s2_1, (180, 20))
            screen.blit(s3_1, (180, 40))
            screen.blit(s4_1, (180, 60))
        if sf_1 == 1:
            s1 = font.render("Подсказка", True, WHITE)
            screen.blit(s1, (50, 20))
        pygame.display.update()
    # 2ая часть конец

    screen.blit(backg_2, (0, 0))
    pygame.display.update()
    time.sleep(0.7)

    screen.blit(image, (650, 100))
    pygame.display.update()
    time.sleep(0.7)

    pygame.draw.polygon(screen, WHITE,
                        [[600, 250], [250, 250], [250, 170], [700, 170], [700, 230], [770, 345], [685, 250]])
    pygame.draw.circle(screen, WHITE, (250, 210), 40)
    pygame.draw.circle(screen, WHITE, (700, 210), 40)
    pygame.display.update()
    time.sleep(0.7)
    font = pg.font.Font(None, 30)

    if count > 25:
        ds = "Спасибо, но я просил всего лишь 25, здесь"
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 180))
            pygame.display.update()
        ds = "явно больше чем нужно."
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 200))
            pygame.display.update()
        score = random.randrange(1000, 2999)

    elif 20 <= count < 25:
        ds = "Спасибо, хоть я и просил 25, это лучше"
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 180))
            pygame.display.update()
        ds = "чем ничего."
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 200))
            pygame.display.update()
        if count == 20:
            score = 5000
        if count == 21:
            score = 6000
        if count == 22:
            score = 7000
        if count == 23:
            score = 8000
        if count == 24:
            score = 9000

    elif count < 20:
        ds = "Спасибо, но тут намного меньше, чем я"
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 180))
            pygame.display.update()
        ds = "просил принести."
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 200))
            pygame.display.update()
        score = random.randrange(3000, 4999)
    else:
        ds = 'Большое спасибо вам, вы собрали ровно 25'
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 180))
            pygame.display.update()
        ds = 'лечебных трав!'
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (260, 200))
            pygame.display.update()
        score = 10000
    ds = 'До новых встреч!'
    ds_1 = ''
    for i in ds:
        ds_1 += i
        gu = font.render(ds_1, True, BLACK)
        time.sleep(ts)
        screen.blit(gu, (260, 220))
        pygame.display.update()
    time.sleep(2.5)
    return score


def game_second():
    screen = pygame.display.set_mode((wl, wh), pygame.NOFRAME)
    pygame.display.set_caption("Hero's Adventure")
    fire_pg = pg.image.load('fire (1).png')

    class Fireball(pg.sprite.Sprite):
        def __init__(self, x, surf, group):
            pg.sprite.Sprite.__init__(self)
            self.image = scale(surf, (50, 50))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect(center=(x, 200))
            # добавляем в группу
            self.add(group)
            self.speed = randint(3, 5)

        def update(self):
            if self.rect.y < wh:
                self.rect.y += self.speed
            else:
                self.kill()

    class Hero_firegame(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.image = scale(pg.image.load('Hero fire.png'), (38, 46))
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect(midbottom=(wl // 2, 1000))

    Fireballs = pg.sprite.Group()
    user = Hero_firegame()

    Maps = ["background1-.jpg", "background2-.jpg", "background3-.jpg"]
    bg_2 = pygame.image.load(Maps[map])
    backg_2 = scale(bg_2, (wl, wh))

    screen.blit(backg_2, (0, 0))
    pg.display.update()
    time.sleep(0.7)

    screen.blit(user.image, user.rect)
    pg.display.update()
    time.sleep(0.7)

    image = scale(pygame.image.load("Fireman.png"), (100, 100))
    image.set_colorkey(WHITE)
    screen.blit(image, (450, 115))
    pygame.display.update()
    time.sleep(0.7)

    pygame.draw.rect(screen, (0, 0, 0), (200, 210, 600, 800), 5)
    pg.display.update()
    time.sleep(0.7)
    run = 1
    font = pg.font.Font(None, 30)
    ps = fs = 0
    st1 = "Вы встретили огенного мага, чтобы одолеть его,"
    st2 = str("вам необходимо добраться до него, уклоняясь от его")
    st3 = str("заклинаний.")
    ST = [st1, st2, st3, ]
    sT = ''
    y = 410
    br = 0
    while run:
        pygame.draw.rect(screen, WHITE, (200, 400, 600, 150))
        pygame.draw.rect(screen, BLACK, (200, 400, 600, 150), 4)
        for i in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 450 <= mouse_x <= 600 and 500 <= mouse_y <= 600:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    br = 1

        for i in range(len(ST)):
            if fs == 1:
                continue
            for j in ST[i]:
                sT += j
                font = pg.font.Font(None, 30)
                q = font.render(sT, True, BLACK)
                time.sleep(0.05)
                screen.blit(q, (220, y))
                pygame.display.update()
            sT = ''
            y += 25
        fs = 1
        font = pg.font.Font(None, 50)
        time.sleep(0.3)
        fast = 'Вперед'
        fast_1 = ''
        for i in fast:
            if ps == 1:
                screen.blit(gj, (210, 270))
                break
            fast_1 += i
            gj = font.render(fast_1, True, BLACK)
            time.sleep(0.05)
            screen.blit(gj, (450, 500))
            pygame.display.update()
        ps = 1
        if br == 1:
            break

    pg.time.set_timer(pg.USEREVENT, 1500)
    go = 0
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pass

            elif i.type == pg.USEREVENT:
                if user.rect.y >= 280:
                    Fireball(randint(210, 790), fire_pg, Fireballs)
                    Fireball(randint(210, 790), fire_pg, Fireballs)
                    Fireball(randint(210, 790), fire_pg, Fireballs)

        screen.blit(backg_2, (0, 0))
        image = scale(pygame.image.load("Fireman.png"), (100, 100))
        image.set_colorkey(WHITE)
        screen.blit(image, (450, 115))
        pygame.draw.rect(screen, (0, 0, 0), (200, 210, 600, 800), 5)
        screen.blit(user.image, user.rect)
        pg.display.update()

        Fireballs.draw(screen)
        Fireballs.update()

        keys = pygame.key.get_pressed()
        if go > 60:
            user.rect.y -= 2
        go += 1
        if keys[pygame.K_LEFT]:
            if 200 <= (user.rect.x - 2) <= 762:
                user.rect.x -= 10

        if keys[pygame.K_RIGHT]:
            if 200 <= (user.rect.x + 2) <= 762:
                user.rect.x += 10

        if user.rect.y <= 200:
            hero_y = 200
            break

        if pg.sprite.spritecollideany(user, Fireballs):
            hero_y = user.rect.y
            break

        pg.display.update()
        pg.time.delay(21)

    ps = fs = 0
    if hero_y == 200:
        st1 = "Поздравляем, с победой над огненным магом!"
        st2 = "Удачи в вашем путешествии!"
    else:
        st1 = "Вы проиграли, огненному магу, не расстраивайтесь!"
        st2 = "Удачи в вашем путешествии!"
    ST = [st1, st2]
    sT = ''
    y = 310
    while True:
        screen.blit(backg_2, (0, 0))
        pygame.draw.rect(screen, WHITE, (250, 300, 550, 150))
        pygame.draw.rect(screen, BLACK, (250, 300, 550, 150), 4)
        for i in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 470 <= mouse_x <= 600 and 390 <= mouse_y <= 445:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if hero_y == 200:
                        return 10000
                    elif 200 < hero_y <= 400:
                        return random.randrange(8000, 9999)
                    elif 400 < hero_y <= 600:
                        return random.randrange(6000, 7999)
                    elif 600 < hero_y <= 800:
                        return random.randrange(4000, 5999)
                    else:
                        return random.randrange(1, 3999)

        for i in range(len(ST)):
            if fs == 1:
                continue
            for j in ST[i]:
                sT += j
                font = pg.font.Font(None, 30)
                q = font.render(sT, True, BLACK)
                time.sleep(0.05)
                screen.blit(q, (265, y))
                pygame.display.update()
            sT = ''
            y += 25
        fs = 1

        font = pg.font.Font(None, 50)
        fast = 'Назад'
        fast_1 = ''
        for i in fast:
            if ps == 1:
                screen.blit(gj, (285, 270))
                break
            fast_1 += i
            gj = font.render(fast_1, True, BLACK)
            time.sleep(0.05)
            screen.blit(gj, (470, 410))
            pygame.display.update()
        ps = 1


def game_third():
    screen = pygame.display.set_mode((wl, wh), pygame.NOFRAME)
    pygame.display.set_caption("MONSTER SHOT")
    score1 = 0
    score2 = 0
    tg = 5
    Maps = ["background1-.jpg", "background2-.jpg", "background3-.jpg"]
    bg_2 = pygame.image.load(Maps[map])
    backg_2 = scale(bg_2, (wl, wh))
    run = 1
    font = pg.font.Font(None, 30)
    screen.blit(backg_2, (0, 0))
    pygame.display.update()
    time.sleep(0.7)
    image = scale(pygame.image.load("Nikto.png"), (300, 500))
    image.set_colorkey(WHITE)
    screen.blit(image, (0, 150))
    pygame.display.update()
    time.sleep(0.7)
    ps = fs = 0
    st1 = "Вы встретили Воришку, вам необходимо догнать его"
    st2 = str("и поймать. Для этого надо набрать 50 очков.")
    st3 = str("(Дабы это сделать необходимо кликать по экрану)")
    ST = [st1, st2, st3]
    sT = ''
    y = 410
    br = 0

    while run:
        pygame.draw.rect(screen, WHITE, (300, 400, 600, 150))
        pygame.draw.rect(screen, BLACK, (300, 400, 600, 150), 4)
        for i in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 500 <= mouse_x <= 600 and 500 <= mouse_y <= 600:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    br = 1

        for i in range(len(ST)):
            if fs == 1:
                continue
            for j in ST[i]:
                sT += j
                font = pg.font.Font(None, 30)
                q = font.render(sT, True, BLACK)
                time.sleep(0.05)
                screen.blit(q, (320, y))
                pygame.display.update()
            sT = ''
            y += 25
        fs = 1
        font = pg.font.Font(None, 50)
        time.sleep(0.3)
        fast = 'Вперед'
        fast_1 = ''
        for i in fast:
            if ps == 1:
                screen.blit(gj, (210, 270))
                break
            fast_1 += i
            gj = font.render(fast_1, True, BLACK)
            time.sleep(0.05)
            screen.blit(gj, (500, 500))
            pygame.display.update()
        ps = 1
        if br == 1:
            break

    while 1:
        screen.blit(backg_2, (0, 0))
        image = scale(pygame.image.load("Nikto.png"), (300, 500))
        image.set_colorkey(WHITE)
        screen.blit(image, (0, 150))
        pygame.draw.rect(screen, WHITE, (300, 200, 600, 150))
        pygame.draw.rect(screen, BLACK, (300, 200, 600, 150), 4)
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                raise SystemExit("QUIT")
            elif i.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 0 <= mouse_x <= 1000 and 0 <= mouse_y <= 1000:
                    score1 += 1

        score1_t = font.render(str(score1), True, BLACK)
        screen.blit(score1_t, (700, 285))
        if tg == 5:
            score2 += randint(0, 1)
            tg = 0
        score2_t = font.render(str(score2), True, BLACK)
        screen.blit(score2_t, (400, 285))
        score2_t1 = font.render("Воришка", True, BLACK)
        screen.blit(score2_t1, (330, 220))
        score1_t1 = font.render(str(hero_name.get_value()), True, BLACK)  #str(hero_name.get_value())
        screen.blit(score1_t1, (650, 220))
        pg.display.update()
        tg += 1
        if score1 == 50:
            win = 1
            break
        if score2 == 50:
            win = 0
            break
        pg.time.delay(21)

    if win == 1:
        screen.blit(backg_2, (0, 0))
        pygame.draw.rect(screen, WHITE, (200, 350, 600, 70))
        pygame.draw.rect(screen, BLACK, (200, 350, 600, 70), 4)
        font = pg.font.Font(None, 30)
        ds = "Поздравляем, вам удалось поймать воришку!"
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (230, 375))
            pygame.display.update()
        pygame.display.update()
        time.sleep(3)
        return random.randrange(5000, 9999)
    else:
        screen.blit(backg_2, (0, 0))
        pygame.draw.rect(screen, WHITE, (200, 350, 600, 70))
        pygame.draw.rect(screen, BLACK, (200, 350, 600, 70), 4)
        font = pg.font.Font(None, 30)
        ds = "К сожалению, воришке удалось убежать."
        ds_1 = ''
        for i in ds:
            ds_1 += i
            gu = font.render(ds_1, True, BLACK)
            time.sleep(ts)
            screen.blit(gu, (230, 375))
            pygame.display.update()
        pygame.display.update()
        time.sleep(3)
        return random.randrange(1000, 4999)


def start_menu():
    global hero_name
    global difficulty

    screen = pygame.display.set_mode((wl, wh), pygame.NOFRAME)
    pygame.display.set_caption("Hero's Adventure")
    menu = pygame_menu.Menu("Hero's Adventure", wl, wh, theme=pygame_menu.themes.THEME_GREEN)

    hero_name = menu.add.text_input('Имя : ', default='Герой')
    difficulty = menu.add.selector('Сложность : ', [('Легко', 1), ('Сложно', 2)])
    menu.add.button('Играть', start_game)
    menu.add.button('Выход', pygame_menu.events.EXIT)

    menu.mainloop(screen)


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = scale(pygame.image.load("Hero.png"), (50, 50))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        self.image = scale(pygame.image.load("Gate.png"), (50, 50))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (950, 950))


class game_1(pg.sprite.Sprite):
    def __init__(self, xs, group):
        pg.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load('Ded.png'), (50, 50))
        self.image.set_colorkey(WHITE)
        self.add(group)
        self.rect = self.image.get_rect()
        self.rect.x = xs * 50
        self.rect.y = random.randrange(0, 20) * 50


class game_2(pg.sprite.Sprite):
    def __init__(self, xw, group):
        pg.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load('Fireman.png'), (50, 50))
        self.image.set_colorkey(WHITE)
        self.add(group)
        self.rect = self.image.get_rect()
        self.rect.x = xw
        self.rect.y = random.randrange(2, 17) * 50


class game_3(pg.sprite.Sprite):
    def __init__(self, xd, group):
        pg.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load('Nikto.png'), (50, 50))
        self.image.set_colorkey(WHITE)
        self.add(group)
        self.rect = self.image.get_rect()
        self.rect.x = xd * 50
        self.rect.y = random.randrange(0, 20) * 50


game_11 = pg.sprite.Group()
game_22 = pg.sprite.Group()
game_33 = pg.sprite.Group()


def generate():
    for i in game_11:
        i.kill()
    for i in game_22:
        i.kill()
    for i in game_33:
        i.kill()
    if (difficulty.get_value()[0][1]) == 1:
        i = 0
        while i != 3:
            game_1(random.choice(spawn_1), game_11)
            game_3(random.choice(spawn_2), game_33)
            i += 1
    else:
        i = 0
        while i != 5:
            game_1(random.choice(spawn_1), game_11)
            game_3(random.choice(spawn_2), game_33)
            i += 1
        game_2(0, game_22)
        game_2(950, game_22)


def start_game():
    global points
    screen = pygame.display.set_mode((wl, wh + 50), pygame.NOFRAME)
    pygame.display.set_caption("Hero's Adventure")
    points = 0
    generate()
    global map
    map = random.randrange(0, 3)
    Gen_map = ["background1.jpg", "background2.jpg", "background3.jpg"]
    bg = pygame.image.load(Gen_map[map])

    backg = scale(bg, (wl, wh))

    hero = Hero(25, 25)
    exit = Exit()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                raise SystemExit("QUIT")
            elif i.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 780 <= mouse_x <= 1000 and 1007 <= mouse_y <= 1007 + 43:
                    start_menu()  # более плавный выход

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if 0 <= (hero.rect.x + step + 50) <= wl:
                hero.rect.x += step

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if 0 <= (hero.rect.x - step) <= wl:
                hero.rect.x -= step

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if 0 <= (hero.rect.y - step) <= wh:
                hero.rect.y -= step

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if 0 <= (hero.rect.y + step + 50) <= wh:
                hero.rect.y += step

        screen.blit(backg, (0, 0))
        pygame.draw.rect(screen, (186, 213, 178), (0, 1000, 1000, 50))
        if difficulty.get_value()[0][1] == 2:
            game_22.draw(screen)
        game_11.draw(screen)
        game_33.draw(screen)
        hero.draw(screen)
        exit.draw(screen)

        namwe = str(hero_name.get_value())
        timer = font.render(namwe, True, WHITE)
        screen.blit(timer, (25, 1007))

        score_1 = "Очки: " + str(points)
        score = font.render(score_1, True, WHITE)
        screen.blit(score, (295, 1007))

        dif_1 = str(difficulty.get_value()[0][0])
        dif = font.render(dif_1, True, WHITE)
        screen.blit(dif, (610, 1007))

        dif_1 = "Выйти"
        dif = font.render(dif_1, True, WHITE)
        screen.blit(dif, (820, 1007))

        if pg.sprite.spritecollideany(hero, game_11):
            for i in game_11:
                if i.rect[0] == hero.rect[0] and i.rect[1] == hero.rect[1]:
                    points += game_first()
                    screen = pygame.display.set_mode((wl, wh + 50), pygame.NOFRAME)
                    i.kill()

        if pg.sprite.spritecollideany(hero, game_22):
            for i in game_22:
                if i.rect[0] == hero.rect[0] and i.rect[1] == hero.rect[1]:
                    points += game_second()
                    screen = pygame.display.set_mode((wl, wh + 50), pygame.NOFRAME)
                    i.kill()

        if pg.sprite.spritecollideany(hero, game_33):
            for i in game_33:
                if i.rect[0] == hero.rect[0] and i.rect[1] == hero.rect[1]:
                    points += game_third()
                    screen = pygame.display.set_mode((wl, wh + 50), pygame.NOFRAME)
                    i.kill()

        if hero.rect[0] == hero.rect[1] == 950:
            time.sleep(0.3)
            End()

        pg.time.delay(75)
        pygame.display.update()


start_menu()
