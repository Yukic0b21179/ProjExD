import pygame as pg
import sys
import random
import tkinter as tk

def main():
    global cnt
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1280, 720))   #Sarface ×ボタンが出なくなるのでサイズ変更
    screen_rct = screen_sfc.get_rect()              #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")      #Sarface
    bgimg_rct = bgimg_sfc.get_rect()                #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    kkimg_sfc = pg.image.load(f"fig/{cnt}.png")          #Sarface 鳥の画像変更
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

        key_states = pg.key.get_pressed()       #キーが押されたとき
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1

        if check_bound(kkimg_rct, screen_rct) != (1, 1):    #チェック関数が通らなかったとき
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1

        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bomb_rct.move_ip(vx, vy)
        ret = check_bound(bomb_rct, screen_rct) #x,y座標がスクリーン画面から超えているかどうか、超えている場合は-1をかける
        vx = vx*ret[0]
        vy = vy*ret[1]

        screen_sfc.blit(bomb, bomb_rct)

        pg.display.update()

        clock.tick(1000)

        if kkimg_rct.colliderect(bomb_rct): break

    global root
    root = tk.Tk()                                                              #gameover画面(y/n)yの場合コンティニュー、nの場合ゲームを終了
    root.geometry("220x100")
    root.title("GameOver")
    label = tk.Label(root, text="continue?", font = ("Times New Roman", 40))
    label.place(y = 90)
    label.pack()
    btn1 = tk.Button(root, text = "Yes", command = Main)
    btn1.place(x = 63, y = 60)
    btn2 = tk.Button(root, text = "No", command = exit)
    btn2.place(x = 126, y = 60)
    root.mainloop()
            

def check_bound(rect, screen):  #スクリーンから出ていない場合は1出ている場合は-1を返す
    a, b = 1, 1
    if rect.left < screen.left or screen.right < rect.right:
        a = -1
    if rect.top < screen.top or screen.bottom < rect.bottom:
        b = -1

    return a, b

root = None
def exit():
    pg.quit()
    sys.exit()

def Main():     #鳥のカウントとゲームオーバー画面の非表示
    global root,cnt
    cnt += 1
    if cnt == 9:
        cnt = 0
    root.destroy()
    main()

if __name__ == "__main__":
    cnt = 0
    pg.init()
    main()


    