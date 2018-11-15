import tkinter
from functools import partial

def welcome(word):
    def say_hi():
        lb.config(text='Hello %s!' % word)
    return say_hi

root = tkinter.Tk()
lb = tkinter.Label(root,text='Hello World!',font=('Arial','20'))
b1=tkinter.Button(root,fg='green',bg='blue',text='botton1',command=welcome('Tedu'))
botton=partial(tkinter.Button,root,fg='green',bg='blue')
b2=botton(text='botton2',command=welcome('China'))
b3=botton(text='quit',command=root.quit)
for item in [lb,b1,b2,b3]:
    item.pack()
root.mainloop()

# if __name__ == '__main__':
#     gui()