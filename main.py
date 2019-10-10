# -*- coding:utf -8 -*-
# !/usr/bin/python3
from tkinter import *
import random
import webbrowser

root = Tk()
root.iconbitmap('p_gen.ico')
root.resizable(width=False, height=False)
root.title("Password Generator v 0.14.51 stable")
root.geometry("420x338+300+300")
calculated_text = Text(root, height=14, width=50)


def erase():
    calculated_text.delete('1.0', END)


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def password():
    for n in range(int(number_entry)):
        password = ''
        for i in range(int(length_entry.get())):
            password += random.choice(chars)
        calculated_text.insert(END, password + "\n")

def info():
    return webbrowser.open('https://coderlog.top/projects.php?id=21')


display_button = Button(text="Generate", command=password)
erase_button = Button(text="Clear", command=erase)
info_button = Button(text="Information", command=info)
text_label = Label(text="CoderLOG Projects (c), 2019 |   Password Generator v 0.14.51 stable      | GNU 3.0", fg="#003363", bg="#99adc0")
number_entry = int(1)

length_entry = Entry(width=10, justify=CENTER)
length_entry.insert(0, "25")

length_label = Label(text="      Password length")
length_label.grid(row=1, column=0, sticky="w")
length_entry.grid(row=1, column=1, padx=1, pady=5)

display_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
erase_button.grid(row=2, column=2, padx=7, pady=5, sticky="w")
info_button.grid(row=2, column=0, padx=12, pady=5, sticky="w")
text_label.place(x=0,y=320)
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)

scrollb = Scrollbar(root, command=calculated_text.yview)
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.configure(yscrollcommand=scrollb.set)

root.mainloop()