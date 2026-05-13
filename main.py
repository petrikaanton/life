
import tkinter as tk
fr = open("glider-gun.txt")
height = int(fr.readline().strip())
width = int(fr.readline().strip())
dish1 = []
dish2 = []

print(height,width)

def create_dishes(height,width):
    global dish1,dish2
    #prazdny
    for i in range(height):
        dish2.append([0]*width)
        dish1.append([0]*width)
    x = 0
    y = 0
    for riadok in fr:
        x = 0
        for znak in riadok.strip():
            if znak != "-":
                dish1[y][x] = 1
            x+=1
        y+=1

def get_neighbors(dish,x,y):
    neighbors = 0

    if x>0 and y>0 and dish[y-1][x-1] == 1:
        neighbors += 1
    if y>0 and dish[y - 1][x] == 1:
        neighbors += 1
    if x<width and y>0 and [y - 1][x+1] == 1:
        neighbors += 1
    if x>0 and dish[y][x-1] == 1:
        neighbors += 1
    if dish[y][x+1] == 1:
        neighbors += 1
    if dish[y + 1][x+1] == 1:
        neighbors += 1
    if dish[y + 1][x+1] == 1:
        neighbors += 1
    if dish[y + 1][x+1] == 1:
        neighbors += 1
    return neighbors

#def coppy_dishes (source, destination)

create_dishes(height,width)
print(dish1)
print(get_neighbors(dish1, 0,0))
