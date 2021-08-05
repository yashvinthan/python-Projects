# importing webbrowser module
import webbrowser
# importing tkinter
from tkinter import *

# creating root
root = Tk()
# setting GUI title
root.title("WebBrowser")
# setting GUI geometry
root.geometry("300x200")


# function to open copyassignment.com in browser
def copyassignment():
    webbrowser.open("www.copyassignment.com")


# function to open google in browser
def google():
    webbrowser.open("www.google.com")


# button to call copyassignment function
copyassignment = Button(root, text="visit copyassignment", command=copyassignment).pack(pady=20)
# button to call google function
mygoogle = Button(root, text="open Google", command=google).pack(pady=20)
root.mainloop()
