import tkinter as Tk
from tkinter import *
from tkinter import Scrollbar, Frame, Text, filedialog, font
root = Tk()
root.title('LexNote')
root.iconbitmap('assets/doc-icon.bmp')                           
root.geometry("1200x660") 
# Set Variable for open file nam #
global open_status_name           
open_status_name = False

global selected 
selected = False
#Create main frame #
my_frame = Frame(root)
my_frame.pack(pady=5)
#create menu 
my_menu = Menu(root)
root.config(menu=my_menu)
# Create scrollbar #
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box #
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16),
    selectbackground="yellow",
    selectforeground="black",  
    undo=True, 
    yscrollcommand=text_scroll.set) 
my_text.pack()

# Configure Scrollbar #

text_scroll.config(command=my_text.yview)


###################### MENU BAR SECTION ######################
###### Subsection: File Menu Functions ######
def new_file():
    # Delete previous text # 
    my_text.delete("1.0", END)
    # Update status bars #
    root.title('New File - LexNote')
    status_bar.config(text="New File" + '   ' + 'LexNote')
    global open_status_name           
    open_status_name = False       

# Open Files # 
def open_file():
    # Delete previous text #
    my_text.delete("1.0", END)
    # Grab Filename #
    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"), ("Markdown Files", "*.md")))
    if text_file:
        #Make filename global
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=f'Saved: {name}  ')
    name = name.replace("C:/gui/", "")
    root.title(f'{name} - TextPad!')
    
    #open the file 
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
# Save As File # 
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".txt*", initialdir="C:/gui/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"), ("Markdown Files", "*.md")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}')
        name = name.replace("C:/gui/", "")
        root.title(f'{name} - LexNote!')
        
        # Save the file # 
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

# Save [as] file #
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file # 
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}  ')
    else:
        save_as_file()
        
############################################## 

###### Subsection: Edit Menu Functions #######
def cut_text(e):
    global selected 
    if my_text.selection_get():
        #Get selected from txtbox
        selected = my_text.selection_get()
        my_text.delete("sel.first", "sel.last")

def copy_text(e):
    global selected
    if my_text.selection_get():
        #Get selected from txtbox
        selected = my_text.selection_get()

def paste_text(e):
    if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)
        pass


###### Subsection: File Menus
# # Add File Menu #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl-S")
file_menu.add_command(label="Save As", command=save_as_file, accelerator="Ctrl+A")
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu #

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+R")

# Add View menu # 

view_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Tool Bar")
view_menu.add_command(label="Status Bar")

# Add Settings Menu # 

settings_menu = Menu(my_menu, tearoff=False)
settings_menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Configure")
settings_menu.add_command(label="Options")
settings_menu.add_command(label="Theme")
settings_menu.add_command(label="Font")

# Add Help Menu #
help_menu = Menu(my_menu , tearoff=False)
my_menu.add_command(label="Help", accelerator="Ctrl+H")
#############################################################

###################### TOOLBAR SECTION ######################
# Add Status Bar to bottom of app #
status_bar = Label(root, text='Ready ' + '     ' + 'LexNote', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

#Edit Bindings
root.bind('<Control-Key-n>', new_file)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-s>', save_file)
root.bind('<Control-Key-a>', save_as_file)

root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-z>', my_text.edit_undo)
root.bind('<Control-Key-r>', my_text.edit_redo)

#### MAIN LOOP ####
root.mainloop() 