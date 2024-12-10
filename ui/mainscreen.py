import tkinter as tk
from tkinter import ttk
from utils.bin_dec_hex_tools import randBin

def displaybin():
    bindisplay.config(text=f"{randBin()} \n{randBin()} \n{randBin()} \n{randBin()} \n{randBin()} ", font=("Arial", 20))
    
def displayhex():
    pass

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)

notebook = ttk.Notebook(window) # Manages a collection of windows/displays

mainTab = tk.Frame(notebook)
baseNTab = tk.Frame(notebook)

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.pack(expand=True, fill='both') # Expand fills space not otherwise used, fill will fill space on x and y axis

exitBtn = tk.Button(mainTab,
                    text='Exit',
                    bg="red",
                    fg="white",
                    activebackground="white",
                    activeforeground="red",
                    command=window.quit,
                    width=20)
exitBtn.place(x=492, y=710)

#Binary Gen
binaryBtn = tk.Button(baseNTab, text='Binary', command=displaybin, width=30, height=5).pack(side="top")

#Hexadecimal Gen
hexBtn = tk.Button(baseNTab, text='Hexadecimal', command=displayhex, width=30, height=5).pack(side="left")

#Binary Display
bindisplay = tk.Label(baseNTab)
bindisplay.pack()

window.mainloop()

