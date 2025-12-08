from tkinter import *
from random import randint
w = Tk()
w.title("Password Generator")
w.geometry("500x400")

def new():
    pw_entry.delete(0,END)
    try:
     length_pw  = int(e.get())
    except ValueError:
       pw_entry.insert(0,"Enter a Number")
       return 
    
    my_pw=''
    for i in range(length_pw):
        my_pw += chr(randint(33,126))
    pw_entry.insert(0,my_pw)


def clip():
    w.clipboard_clear()
    w.clipboard_append(pw_entry.get())

lf=LabelFrame(w, text="Enter Your Desi")
lf.pack(pady=20)

e=Entry(lf, font=("Times", 24), width=5)
e.pack(pady =30 ,padx=30)

pw_entry=Entry(w, text ='',font=("Times", 24),width=13)
pw_entry.pack(pady=20)

f=Frame(w)
f.pack(pady = 20)

b1= Button(f, text="Generate a Strong Password",command=new)
b1.grid(row=0,column=0)

b2=Button(f, text="Copy To Clipboard",command=clip)
b2.grid(row = 0 ,column=1,padx=20)




w.mainloop()