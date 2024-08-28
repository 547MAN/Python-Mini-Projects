from tkinter import *

#--------------Window-----------
root =Tk()

#Ovveride the setting of the window

#Change background color by using bg. - MUST use aviable values from a list.
root.configure(bg="navyblue")

#Size the window
root.geometry("1024x780")

#window Title
root.title("Mine Sweeper-2024")

#Locks resizing out, first False for the Width, and secound False for the height
root.resizable(False, False)


top_frame1of3=Frame(
    root,
    bg="yellow", #Change later to navyblue
    width=1024,
    height=90
)
top_frame2of3=Frame(
    root,
    bg="red", #Change later to navyblue
    width=1024,
    height=90
)
top_frame3of3=Frame(
    root,
    bg="green", #Change later to navyblue
    width=1024,
    height=90
)

top_frame1of3.place(x=0,y=0)
top_frame2of3.place(x=0,y=90)
top_frame3of3.place(x=0,y=180)

#Run the window
root.mainloop()
#--------------Window-----------
