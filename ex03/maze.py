from tokenize import maybe
import maze_maker
import tkinter as tk

def key_down(event):
    global key 
    key = event.keysym

def key_up(event):
    global key 
    key = ""

def main_proc():
    global cx,cy,key,mx,my

    if key != "":

        delta = {   #キー：押されているキーkye/値：移動幅リスト[x,y]
            "Up"    : [0, -1],
            "Down"  : [0, +1],
            "Left"  : [-1, 0],
            "Right" : [+1, 0],
        }

        mx, my = mx + delta[key][0], my + delta[key][1]
    
        if list[my][mx] == 0:

            cx, cy = mx*100 + 50, my*100 +50

            canvas.coords("tori", cx, cy)

        else:
            mx, my = mx - delta[key][0], my - delta[key][1]
            
    root.after(100, main_proc)

if __name__ == "__main__":

    mx, my = 1, 1

    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    list = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,list)

    tori = tk.PhotoImage(file = "fig/6.png")

    cx, cy = mx * 100 + 50,my * 100 + 50
    canvas.create_image(cx, cy, image = tori, tag = "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()

    jid = 0

    root.mainloop()