import tkinter
from functools import partial

def gui():
    root = tkinter.Tk()
    lb = tkinter.Label(root,text='Hello World!')
    b1=tkinter.Button(root,fg='green',bg='blue',text='botton1')
    botton=partial(tkinter.Button,root,fg='green',bg='blue')
    b2=botton(text='botton2')
    b3=botton(text='quit',command=root.quit)
    for item in [lb,b1,b2,b3]:
        item.pack()
    root.mainloop()

if __name__ == '__main__':
    gui()