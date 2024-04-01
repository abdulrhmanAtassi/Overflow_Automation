import customtkinter as ctk
import os 
from tkinter import filedialog

window = ctk.CTk()
window.title('Backup')
window.geometry('400x300')

def Backup():
    root = folder_path.get()
    


input = ctk.CTkEntry(
    window,
)

btn = ctk.CTkButton(
    window,
    text="Backup",
    command = Backup
    
)

def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

folder_path = ctk.StringVar()

button2 = ctk.CTkButton(
    window,
    text="Browse",
    command=browse_button
)

input.pack(pady=10)
btn.pack(pady=5)
button2.pack(pady=5)

window.mainloop()