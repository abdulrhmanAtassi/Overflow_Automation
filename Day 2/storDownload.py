
import os
import tkinter as tk

window = tk.Tk()
window.title('Sort Download')
window.geometry('400x300')


def organize():
    root = dirEntry.get()
    files = os.listdir(root)
    print(os)   
    for f in files:
        #ext = f.split('.')[-1]
        ext = os.path.splitext()[1]
        
        
    

dirEntry = tk.Entry(
    window,
)

btn = tk.Button(
    window,
    text="Sort",
    command= organize
)


label_1 = tk.Label(
    window,
    text= 'Welcome to the directory organizer',
    font= ('',20,'bold'),
    foreground= 'grey'
) 

label_2 = tk.Label(
    window,
    text= 'Write the dir for the file u wanna to sort',
    font= ('',15,''),
    foreground= 'grey'
) 

label_1.pack(pady= 10)
label_2.pack(pady= 10)
dirEntry.pack(pady= 10)
btn.pack(pady= 10)
window.mainloop()