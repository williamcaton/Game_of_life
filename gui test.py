import tkinter as tk
from tkinter import *
import time

window = tk.Tk()#setup window
window.title('test')

size_of_grid = 10
number_of_cycles = 20
grid = [['_' for x in range(size_of_grid)] for y in range(size_of_grid)]
temp_grid = [['_' for x in range(size_of_grid)] for y in range(size_of_grid)]
grid[1][2] = 'X'
grid[2][2] = 'X'
grid[3][2] = 'X'
grid[3][1] = 'X'
grid[2][0] = 'X'

for a in range(number_of_cycles):
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            temp_grid[y][x] = grid[y][x]
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            neighbours = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if ((y+j)>=0)and((y+j)<size_of_grid)and((x+i)>=0)and((x+i)<size_of_grid):
                        if grid[y+j][x+i] == 'X':
                            neighbours+=1
            if grid[y][x] == 'X':
                neighbours-=1
            if (neighbours < 2) or (neighbours > 3):
                temp_grid[y][x]='_'
            if neighbours == 3:
                temp_grid[y][x]='X'
    for x in range(size_of_grid):
        for y in range(size_of_grid):
            grid[y][x] = temp_grid[y][x]

    for i in range(size_of_grid):
        for j in range(size_of_grid):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=str(grid[j][i]))
            label.pack()
    #time.sleep(0.5)
    window.update()

"""
lbl=Label(window,text='hello',font=('Arial Bold',15))
lbl.grid(column=2, row=2)
window.geometry('1000x1000')

def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=5, row=0)

# configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="X")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
"""

