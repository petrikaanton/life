import tkinter as tk, random
win = tk.Tk()
win.title("kable")

velkost = 600
colors = ["green", "red", "grey", "blue", "orange"]
wires = []
cas = 5
stop = False

canvas = tk.Canvas(win, height=velkost, width=velkost)
canvas.pack()

hodiny = canvas.create_text(300, 150, text=cas, font=("Arial", 40, "bold"))

for i in range(len(colors)):
    wires.append(canvas.create_rectangle(200,200+10*i,400,210+10*i,fill=colors[i],width=2))

def click(event):
    global stop
    object = canvas.find_overlapping(event.x, event.y,event.x+1, event.y+1)
    if winner in object:
        stop = True
        canvas.create_text(300,300,text="Vyhral si",font=("Arial",90,"bold"))

def timer():
    global cas
    global stop
    cas -= 1
    canvas.itemconfig(hodiny, text=cas)
    if cas <= 0:
        stop = True
        canvas.create_text(300, 300, text="Vybuchol si", font=("Arial", 70, "bold"))
    if stop == False:
        canvas.after(1000, timer)

winner = random.choice(wires)
print(winner-1)

canvas.bind("<Button-1>", click)
timer()

win.mainloop()