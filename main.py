import tkinter as tk
import tkinter.messagebox
import os
from tkinter import filedialog
def select_file():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def organize():
    directories = ["Multimedia", "Text", "Compress"]
    
    path = path_label.cget("text")
    
    for dire in directories:
        dire_path = os.path.join(path, dire)
        if not os.path.exists(dire_path):
            os.makedirs(dire_path)
            
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            if ext in [".jpg", ".jpeg", ".png", ".ico", ".svg", ".mp3", ".mp4", ".mov", ".webm"]:
                dest_path = os.path.join(path, "Multimedia", file)
                os.replace(os.path.join(path, file), dest_path)
            elif ext in [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsm", ".xlsx", ".ods"]:
                dest_path = os.path.join(path, "Text", file)
                os.replace(os.path.join(path, file), dest_path)
            elif ext in [".zip", ".rar", ".tar.gz"]:
                dest_path = os.path.join(path, "Compress", file)
                os.replace(os.path.join(path, file), dest_path)
    tkinter.messagebox.showinfo("OrganizeMe",  "Complete!")
    

def toggle_mode():
    current_mode = mode_var.get()
    new_mode = "dark" if current_mode == "light" else "light"
    mode_var.set(new_mode)
    set_color_scheme()

def set_color_scheme():
    current_mode = mode_var.get()
    if current_mode == "light":
        bg_color = "white"
        text_color = "black"
    else:
        bg_color = "#333333"
        text_color = "white"
    window_width = 550
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # Update colors for all widgets
    root.configure(bg=bg_color)
    title.configure(bg=bg_color, fg=text_color)
    desc.configure(bg=bg_color, fg=text_color)
    path_label.configure(bg=bg_color, fg=text_color)
    button_frame.configure(bg=bg_color)
    creator_label.configure(bg=bg_color, fg=text_color)

    # Widgets

root = tk.Tk()
root.title("OrganizeMe")
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)

mode_var = tk.StringVar()
mode_var.set("dark")

mode_button = tk.Button(root, text="Mode", command=toggle_mode)
mode_button.pack(pady=5, side="top", anchor="ne")

title = tk.Label(root, text="Welcome to OrganizeMe", font=("Helvetica", 18, "bold"))
title.pack()
desc = tk.Label(root, text="Select the directory to organize:", font=("Helvetica", 15))
desc.pack()

path_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"))
path_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

select_button = tk.Button(button_frame, text="Select", command=select_file)
select_button.pack(side="left", padx=5)

organize_button = tk.Button(button_frame, text="Organize", command=organize)
organize_button.pack(side="left", padx=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="right")

creator_label = tk.Label(bottom_frame, text="Created by Daniel Ruiz Gtz", font=("Helvetica", 8, "italic"))
creator_label.bind("<Button-1>", lambda event: os.system("start https://github.com/Daniel-Ruiz-Gtz"))
creator_label.config(cursor="hand2")
creator_label.pack()


set_color_scheme()
root.mainloop()
