from tkinter import *
import settings
import utils
from cell import Cell
#--------------Window-----------
root =Tk()

#Ovveride the setting of the window

#Change background color by using bg. - MUST use aviable values from a list.
root.configure(bg="black")

#Size the window
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

#window Title
root.title("Mine Sweeper-2024")

#Locks resizing out, first False for the Width, and secound False for the height
root.resizable(False, False)


#Frame at the top
top_frame1of3=Frame(
    root,
    bg="black", #Change later to navyblue
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

top_frame1of3.place(x=0,y=0)

#frame at the left
left_frame=Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0,y=utils.height_prct(25))

center_frame= Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25))




for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
#Run the window
root.mainloop()
#--------------Window-----------
