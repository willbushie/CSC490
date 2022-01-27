# CSC 490 - Wallpaper assignemnt V1

# import tkinter
import tkinter
import math

# create canvas variables to draw the picture
win=tkinter.Tk()
#win.geometry("1000x1000")
myCanvas = tkinter.Canvas(win)
myCanvas.pack()

# write one pixel to the image
def plot_pixel(x,y,r,canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x - r
    y1 = y - r
    return canvasName.create_oval(x0,y0,x1,y1)
    
# our program - wallpaper | red yellow blue for V3
def wallpaper():
    corna = 5
    cornb = 5
    side = 3
    for i in range(1000):
        for j in range (1000):
            x = corna + i * side/10
            y = cornb + j * side/10
            c = math.floor(x * x + y * y)
            if (c%2 == 0):
                plot_pixel(i, j, 1, myCanvas)

# calling our wallpaper function
wallpaper()

win.mainloop()
