import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

window_width = 400
window_hight = 400

monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()

x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
root.title("JPEG To PNG Converter")
root.iconbitmap("JK.ico")
root.config(bg="#dbdbdb")


def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files","*.jpg")])
    file_path_label.config(width=35, text=file_path)

def select_save_path():
    global save_path
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("PNG files", "*.png")])
    save_path_label.config(width=35, text=save_path)

def reset():
    messagebox.showinfo("Info", "File conversion successful!")
    time.sleep(3)
    root.title("JPEG To PNG Converter")
    result_label.config(text="")
    file_path_label.config(text="")
    save_path_label.config(text="")

def convert():
    global duration
    if file_path.endswith(".jpg"):
        if save_path:
            root.title("Converting File...")
            with Image.open(file_path) as img:
                img.save(save_path)
            result_label.config(text="Conversion successful!")
            reset()
        else:
            result_label.config(text="Please select a save path")
    else:
        result_label.config(text="Please select a JPEG file")


file_path_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
file_path_label.pack(pady=5)

file_select_button = Button(root, text="Select JPEG File", font=("arial", 12), width=20, command=select_file)
file_select_button.pack(pady=0)

save_path_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
save_path_label.pack(pady=0)

save_path_button = Button(root, text="Select Save Path", font=("arial", 12), width=20, command=select_save_path)
save_path_button.pack(pady=5)

result_label = Label(root, font=("arial", 12), bg="#dbdbdb", text="")
result_label.pack()

convert_button = Button(root, font=("arial", 12), width=20, text="Convert to PNG", command=convert)
convert_button.pack(pady=30)

root.mainloop()
