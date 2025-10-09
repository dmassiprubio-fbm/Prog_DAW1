import tkinter as tk

windows = tk.Tk()
windows.title('HALLOWEEN 2024')

canvas = tk.Canvas(windows, width=400, height=400, bg='black')
canvas.pack()

canvas.create_text(200, 50, text='Feliz Halloween 💀', fill='white', font=('Arial', 30))

canvas.create_oval(50, 150, 350, 350, fill='orange' , outline='')

canvas.create_polygon(140,175, 175,235, 95,225, fill = 'black' )
canvas.create_polygon(260,175, 295,225, 215,235, fill = 'black' )

canvas.create_polygon(200,280, 170,250, 230,250, fill = 'black' )

canvas.create_polygon(
    260,300,
    240,320,
    220,300,
    200,320,
    180,300,
    160,320,
    140,300,
)

canvas.create_rectangle(0,350,400,400, fill='green')
canvas.create_rectangle(0,0,10,10, fill='red')

def show_boo(event=None):
    boo_text = canvas.create_text(200,100, text='DAVID MUERE EN EL VIAJE DE ESTUDIOS!!', fill='Red', font=('Helvetica', 13))
    canvas.after(5000, canvas.delete, boo_text)

canvas.bind('<Button-1>', show_boo)



windows.mainloop()
