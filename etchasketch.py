from tkinter import *

root = Tk()
root.title("Etch-a-Sketch")
root.geometry("1000x800+10+10")
root.config(bg="teal")

'''MODEL'''
def draw_line(event):
    canvas.create_line(oldx.get(),oldy.get(),x.get(),y.get(),fill = hex_color.get(),width = 5)
    oldx.set(x.get())
    oldy.set(y.get())

def change_color(event):
    hex_color.set(f"#{red.get():02x}{green.get():02x}{blue.get():02x}")

def clear_canvas():
    canvas.delete('all')

red = IntVar()
red.set(255)

green = IntVar()
green.set(255)

blue = IntVar()
blue.set(255)

hex_color = StringVar()
hex_color.set(f"#{red.get():02x}{green.get():02x}{blue.get():02x}")

oldx = IntVar()
oldx.set(475)

oldy = IntVar()
oldy.set(300)

x = IntVar()
x.set(475)

y = IntVar()
y.set(300)

'''CONTROLLER'''
red_slider = Scale(root,bg = "red", fg = "white", from_ = 0, to = 255, orient = "horizontal", variable = red, command = change_color)
red_slider.place(x = 20, y = 60, width = 300, height = 50)

green_slider = Scale(root,bg = "green", fg = "white", from_ = 0, to = 255, orient = "horizontal", variable = green, command = change_color)
green_slider.place(x = 353, y = 60, width = 300, height = 50)

blue_slider = Scale(root,bg = "blue", fg = "white", from_ = 0, to = 255, orient = "horizontal", variable = blue, command = change_color)
blue_slider.place(x = 667, y = 60, width = 300, height = 50)

x_slider = Scale(root, bg = "teal", fg = "white", orient = "horizontal", from_ = 0, to = 900, variable = x, command = draw_line, borderwidth= 0, highlightthickness=0)
x_slider.place(x = 20, y = 120, width = 900, height = 50)

y_slider = Scale(root, bg = "teal", fg = "white", from_ = 0, to = 600,  variable = y, command = draw_line, borderwidth= 0, highlightthickness=0)
y_slider.place(x = 930, y = 180, width = 50, height = 600)

clear = Button(root, bg = "teal", fg = "white", text = "Clear", command = clear_canvas)
clear.place(x=930,y=120,width=50,height = 50)

'''VIEW'''
title = Label(root, bg = "teal",fg="white",text = "Etch-a-Sketch", font = ("Times New Roman", 30))
title.place(x=350, y = 10, width = 300, height = 50)

canvas = Canvas(root, bg = "black")
canvas.place(x=20,y=180,width=900,height=600)





root.mainloop()