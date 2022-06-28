from tokenize import maybe
import maze_maker
import tkinter as tk

def count_down():     #カウントダウン関数　一秒ごとにtmrのカウントを-1する。
    global tmr
    tmr -= 1
    canvas.create_text(400, 50, text = f"制限時間：{tmr}", font = ("Times New Roman", 80), tag = "制限時間")

def key_down(event):    #キーが押されたら
    global key 
    key = event.keysym

def key_up(event):      #キーが離されたら
    global key 
    key = ""

def main_proc():    #キャラクターの座標の関する処理
    global cx,cy,key,mx,my,cnt

    if key != "":

        delta = {   #キー：押されているキーkye/値：移動幅リスト[x,y]
            "Up"    : [0, -1],
            "Down"  : [0, +1],
            "Left"  : [-1, 0],
            "Right" : [+1, 0],
        }

        mx, my = mx + delta[key][0], my + delta[key][1]
    
        if list[my][mx] == 0:   #マスのリストが床判定だったら

            cx, cy = mx*100 + 50, my*100 +50

            canvas.coords("tori", cx, cy)

        else:
            mx, my = 1, 1
            cx, cy = mx*100 + 50, my*100 +50
            canvas.delete("tori")
            canvas.create_image(cx, cy, image = tori, tag = "tori")

    cnt += 1
            
    if cnt == 10:   #一秒後
        canvas.delete("制限時間")
        cnt = 1
        count_down()

    root.after(100, main_proc)

if __name__ == "__main__":

    cnt = 1

    mx, my = 1, 1

    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    list = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,list)

    tori = tk.PhotoImage(file = "fig/6.png")
    tori2 = tk.PhotoImage(file = "fig/6.png")

    cx, cy = mx * 100 + 50,my * 100 + 50
    canvas.create_image(cx, cy, image = tori, tag = "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()

    jid = 0

    # label = tk.Label(root, text="制限時間", font = ("Times New Roman", 80))
    # label.pack()
    tmr = 100
    count_down()

    root.mainloop()