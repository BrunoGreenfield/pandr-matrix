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

announcementVar=tk.StringVar()
def submit():
    announcement=announcementVar.get()
    #("    ANNOUNCEMENT    " + announcement + "    ANNOUNCEMENT    ")
    screenPrev.config(text=announcement)
    announcementVar.set("")
    
announcementEntry = tk.Entry(mainTab,
                             textvariable = announcementVar,
                             font=('DejaVu Sans',10,'normal'))
subBtn=tk.Button(mainTab,text = 'Submit', command = submit)
screenPrev = tk.Label(mainTab)

announcementEntry.pack()
subBtn.pack()
screenPrev.pack()


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
