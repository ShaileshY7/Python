import tkinter as tk
from tkinter import filedialog,messagebox

# main window
root=tk.Tk()
root.title("Simple text Editor")
root.geometry("800x600")

# text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12)
)

text.pack(expand=True,fill=tk.BOTH)

# main logic start here
# Function-1 to create anew file
def new_file():
    text.delete(1.0,tk.END)

# function-2 to open new file

def open_file():
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
    )

    if file_path:
        #open file
        with open(file_path,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())


#   Function-3 save the file
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))

        messagebox.showinfo("Info","File saved successfully")


# Create Menu Bar
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

# New, open ,save and exit

# add filemenu to menubar
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# start and keeps the window open
root.mainloop()