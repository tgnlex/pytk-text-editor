import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import Scrollbar, Frame
from tkinter import Text
root = Tk()
root.title('LexNote')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1200x660")
#Create main frame 
my_frame = Frame(root)
my_frame.pack(pady=5)
# Create scrollbar 
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
# Create Text Box 
my_text = Text(my_frame, 
    width=97, height=25, 
    font=("Helvetica", 16),
    selectbackground="yellow",
    selectforeground="black",)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)

root.mainloop()