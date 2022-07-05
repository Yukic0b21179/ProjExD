import pygame as pg
import sys
import random

def main():

    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1280, 720))   #Sarface ×ボタンが出なくなるのでサイズ変更
    screen_rct = screen_sfc.get_rect()              #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")      #Sarface
    bgimg_rct = bgimg_sfc.get_rect()                #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png")          #Sarface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()                #Rect
    kkimg_rct.center = 900, 400
    screen_sfc.blit(kkimg_sfc, kkimg_rct)

    vx , vy = 1, 1

    bomb = pg.Surface((20,20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb, (255, 0, 0), (10,10), 10)
    bomb_rct = bomb.get_rect()                #Rect
    bomb_rct.centerx = random.randint(0, screen_rct.width)
    bomb_rct.centery = random.randint(0, screen_rct.height)
    screen_sfc.blit(bomb, bomb_rct)
    
    pg.display.update()


    clock.tick(0.5)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1

        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1

        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bomb_rct.move_ip(vx, vy)
        ret = check_bound(bomb_rct, screen_rct)
        vx = vx*ret[0]
        vy = vy*ret[1]

        screen_sfc.blit(bomb, bomb_rct)

        pg.display.update()

        clock.tick(1000)

        if kkimg_rct.colliderect(bomb_rct): return
            

def check_bound(rect, screen):
    a, b = 1, 1
    if rect.left < screen.left or screen.right < rect.right:
        a = -1
    if rect.top < screen.top or screen.bottom < rect.bottom:
        b = -1

    return a, b

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()