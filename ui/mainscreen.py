import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1024, height=768) # We will want to change this to the resolution of our monitor

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

window.mainloop()
