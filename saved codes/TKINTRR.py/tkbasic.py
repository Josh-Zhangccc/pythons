import tkinter as tk

root =tk.Tk()
root.title('1')
root.geometry('400x200')#是’x‘！
var=tk.StringVar()
label=tk.Label(root,textvariable=var,text='OMG!ITS TK!',bg='green',font=('Arial',12),width=15,height=5)
label.pack()
on_hit=False
def hit():
    global on_hit
    if on_hit==True:
        on_hit=False
        var.set('')
    else:
        on_hit=True
        var.set('You hit me')

button=tk.Button(root,text='hit me',width=15,height=2,command=hit)
button.pack()

root.mainloop()#持续刷新（while）
