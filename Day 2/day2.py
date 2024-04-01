import tkinter as tk

window = tk.Tk()
window.title('my First GUI')
window.geometry('400x300')

def on_click():
    name = input.get()
    label_1.config(
        text= f"Hello {name}!"
    )
    

input = tk.Entry(
    window,
)

btn = tk.Button(
    window,
    text="Send",
    command = on_click
    
)

label_1 = tk.Label(
    window,
    
    text= 'Hello',
    font= ('',20,'bold'),
    foreground= 'grey'
) 
label_1.pack()
input.pack()
btn.pack()



window.mainloop()
