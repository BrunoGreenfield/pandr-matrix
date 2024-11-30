import tkinter as tk
from tkinter import ttk
from utils.bin_dec_hex_gen import randBin

def displaybin():
    bindisplay.config(text=randBin())

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)

notebook = ttk.Notebook(window) # Manages a collection of windows/displays

mainTab = tk.Frame(notebook)
baseNTab = tk.Frame(notebook)

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.pack(expand=True, fill='both') # Expand fills space not otherwise used, fill will fill space on x and y axis

exitBtn = tk.Button(mainTab, text='Exit', command=window.quit, width=20)
exitBtn.pack()

binaryBtn = tk.Button(baseNTab, text='Binary', command=displaybin, width=20)
binaryBtn.pack()

bindisplay = tk.Label(baseNTab)
bindisplay.pack()

window.mainloop()

