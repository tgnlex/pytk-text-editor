from tkinter import * 

root = Tk()
root.title("Entry Boxes")
root.geometry("700x500")
root.iconbitmap('assets/doc-icon.bmp')

my_label = Label(root, text="Enter Something", font=("Helvetica", 24))
my_entries = []

def something():
    entry_list = ""
    
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + "\n"
        my_label.config(text=entry_list)
    print(my_entries[24].get())
    
#Row Loop 
for y in range(5):
    #Column Loop
    for x in range(5):
        my_entry = Entry(root)
        my_entry.grid(row=y, column=x, pady=20, padx=5)
        my_entries.append(my_entry)
        