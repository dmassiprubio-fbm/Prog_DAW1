import tkinter as tk
import random

root = tk.Tk()
root.title('Abre de Nadal')

canvas_width = 800
canvas_heigth = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_heigth, bg='black')
canvas.pack()

tree_color = 'green'
canvas.create_polygon(canvas_width/2, 100,
                      200, 500,
                      600, 500,
                      fill=tree_color)

trunk_width = 80
x1 = canvas_width / 2 - trunk_width / 2
y1 = 500
x2 = canvas_width / 2 + trunk_width / 2
y2 = canvas_heigth
canvas.create_rectangle(x1, y1, x2, y2, fill='brown')

radius = random.randint(5,15)

ornaments = [[400,100], [350,200], [450,200], [400,200]]

ornament_colors = ['red', 'gold', 'blue', 'silver', 'pink']
color = random.choice(ornament_colors)

for ornament in ornaments:
    canvas.create_oval(ornament[0]-radius, ornament[1]-radius,ornament[0]+radius, ornament[1]+radius, fill = color)

snowflakes = []

for i in range(100):
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_heigth)
    snowflakes.append([x, y])

for flake in snowflakes:
    x=flake[0]   
    y=flake[1]
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='white', outline='white', tags='snow')
    

root.mainloop()

