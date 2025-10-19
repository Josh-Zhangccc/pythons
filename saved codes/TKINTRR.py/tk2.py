import tkinter as tk
window=tk.Tk('400x400')
e=tk.Entry(window,show='*')
t=tk.Text(window,height=2)
def insert1():
    var=e.get()
    t.insert('insert',var)
def insert2():
    var=e.get()
    t.insert('end',var)
button1=tk.Button(window,text='insert point',width=15,height=2,command=insert1)
button2=tk.Button(window,text='insert end',width=15,height=2,command=insert2)
e.pack()
button1.pack()
button2.pack()
t.pack()
window.mainloop()
