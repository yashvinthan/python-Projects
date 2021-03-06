from tkinter import *

root = Tk()
root.geometry("700x700")
root.title("Changing screen size")
root.minsize(400, 600)
root.maxsize(700, 800)

subject = Label(root, text="You can change screen size according        
to your wish", font="comicsansms 13 bold", borderwidth=3, relief=SUNKEN)

can_width = StringVar()
can_height = StringVar()


def update():
    root.geometry(f"{can_width.get()}x{can_height.get()}")


width = Label(root, text="Enter width")
height = Label(root, text=" Enter height")
width_entry = Entry(root, textvariable=can_width)
height_entry = Entry(root, textvariable=can_height)
width.grid(row=0, column=0)
height.grid(row=1, column=0)
width_entry.grid(row=0, column=1)
height_entry.grid(row=1, column=1)
Button(root, text="Apply", command=update).grid(row=2, column=1, pady=12)
subject.grid(row=3, column=1, pady=12)

root.mainloop()