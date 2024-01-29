import tkinter as tk

def toggle_mode():
    current_mode = mode_var.get()
    new_mode = "dark" if current_mode == "light" else "light"
    mode_var.set(new_mode)
    set_color_scheme()

def set_color_scheme():
    current_mode = mode_var.get()
    if current_mode == "light":
        # Light mode color scheme
        bg_color = "white"
        text_color = "black"
    else:
        # Dark mode color scheme
        bg_color = "#333333"
        text_color = "white"
    # Update colors for all widgets
    root.configure(bg=bg_color)
    title.configure(bg=bg_color, fg=text_color)
    desc.configure(bg=bg_color, fg=text_color)
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root = tk.Tk()
root.title("OrganizeMe")

mode_var = tk.StringVar()
mode_var.set("dark")  # Default mode is light

mode_button = tk.Button(root, text="Dark/Light", command=toggle_mode)
mode_button.pack(pady=10, side="top", anchor="ne")

title = tk.Label(root, text="Welcome to OrganizeMe", font=("Helvetica", 18))
title.pack()
desc = tk.Label(root, text="Select the directory to organize:", font=("Helvetica", 12))
desc.pack()


set_color_scheme()
root.mainloop()
