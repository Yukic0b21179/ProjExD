import pygame as pg
import sys
import random
import tkinter as tk


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


def main():
    bgn = int(pg.time.get_ticks())
    global counter,fcnt

    clock = pg.time.Clock()
    scr = Screen("fighting！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)
    old = 0
    fonto = pg.font.Font("C:\WINDOWS\FONTS\BIZ-UDMINCHOM.TTC", 80)

    while True:
        scr.blit()
        fcnt += 1

        sec = int(100-(pg.time.get_ticks()-bgn)/1000)
        if sec == 0:
                clear()
        txt = fonto.render(f"制限時間{sec}", True, (255,0,0))
        scr.sfc.blit(txt, (200, 100))

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            break

        pg.display.update()
        clock.tick(1000)



def Continue():
    global root
    root = tk.Tk()                                                              #gameover画面(y/n)yの場合コンティニュー、nの場合ゲームを終了
    root.geometry("220x100")
    root.title("GameOver")
    label = tk.Label(root, text="continue?", font = ("Times New Roman", 40))
    label.place(y = 90)
    label.pack()
    btn1 = tk.Button(root, text = "Yes", command = reset)
    btn1.place(x = 63, y = 60)
    btn2 = tk.Button(root, text = "No", command = exit)
    btn2.place(x = 126, y = 60)
    root.mainloop()


def clear():
    global root
    root = tk.Tk()
    root.geometry("400x110")
    root.title("ゲームクリア！")
    label = tk.Label(root, text="Congratulations!", font = ("Times New Roman", 40))
    label.place(y = 90)
    label.pack()
    btn = tk.Button(root, text = "おめでとう！", command = exit)
    btn.place(x = 150, y = 65)
    root.mainloop()


def reset():     #鳥のカウントとゲームオーバー画面の非表示
    global root
    root.destroy()
    pg.init()
    main()


def exit():
    pg.quit()
    sys.exit()


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    cnt = 0
    fcnt = 0
    tmr = 100
    clock = pg.time.Clock()
    crashed = False
    counter = 100
    pg.init()
    main()
    while True:
        Continue()