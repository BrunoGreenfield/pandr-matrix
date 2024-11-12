import tkinter as tk

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1024, height=768) # We will want to change this to the resolution of our monitor

exitBtn = tk.Button(window, text='Exit', command=window.quit, width=20)
exitBtn.pack()

window.mainloop()
