from tkinter import Label, Button, Tk, Entry
from hashlib import md5
from os import system
from sys import exit

def main(*args):
    pas = usr.get()
    enc = md5(pas.encode()).hexdigest()
    tom = "0164fc7d23466b1a68408d0744239b6e"
    if enc == tom:
        system("%windir%\explorer.exe microsoft-edge:http://web.whatsapp.com")
    exit()

tk = Tk()
tk.resizable(0, 0)
tk.overrideredirect(True)
tk.state('zoomed')
tk.config(bg='black')

Label(tk, text='Enter Your Password :-', font='Arial 30 bold', bg='black', fg='white').place(x=150, y=100)

usr = Entry(tk, font='Arial 30 bold', border=20)
usr.focus()
usr.pack(padx=50, pady=200, ipadx=300, ipady=20)

Button(tk, text='Submit', bg='green', fg='white', font='Arial 20 bold', command=main).place(x=300, y=600, height=75, width=150)
Button(tk, text='Exit', bg='red', fg='white', font='Arial 20 bold', command=exit).place(x=900, y=600, height=75, width=150)

tk.bind("<Escape>", exit)
tk.bind("<Return>", main)
tk.mainloop()
