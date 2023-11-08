import tkinter
from tkinter import *
from functools import partial
import math

def add(sm, x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    add = int(num1) + int(num2)
    sm.config(text='Answer =  %d' %add)
    return


def subtract(sm, x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    subtract = int(num1) - int(num2)
    sm.config(text='Answer =  %d' %subtract)
    return

def mult(sm, x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    mult = int(num1) * int(num2)
    sm.config(text='Answer =  %d' %mult)
    return

def div(sm, x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    div = int(num1) / int(num2)
    sm.config(text='Answer =  %f' %div)
    return

def percent(sm,x1):
    num = x1.get()
    percent = int(num) / 100
    sm.config(text='Answer = %f' %percent)
    return

def log(sm,x1):
    num = x1.get()
    log = math.log(float(num),10)
    sm.config(text = 'Answer = %f' %log)
    return

def power(sm,x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    power = int(num1) ** int(num2)
    sm.config(text='Answer = %f' %power)
    return

def root(sm,x1,x2):
    num1 = x1.get()
    num2 = x2.get()
    root = int(num1) ** (1/int(num2))
    sm.config(text='Answer = %f' %root)
    return

def sine(sm,x1):
    num = x1.get()
    angle = math.radians(float(num))
    sine = math.sin(angle)
    sm.config(text='Answer = %f' %sine)
    return
    
def cosine(sm,x1):
    num = x1.get()
    angle = math.radians(float(num))
    cosine = math.cos(angle)
    sm.config(text='Answer = %f' %cosine)
    return

def tangent(sm,x1):
    num = x1.get()
    angle = math.radians(float(num))
    tangent = math.tan(angle)
    sm.config(text='Answer = %f' %tangent)
    return

def mod(sm, x1):
    num = x1.get()
    mod = abs(float(num))
    sm.config(text='Answer = %f' %mod)
    return

win = Tk()
win.geometry('300x350')
win.title("Calculator")

x1 = StringVar()
x2 = StringVar()

l1 =  Label(win, text='Number 1 ',font=5)
l1.place(x=1,y=1)
e1 = Entry(win, background='grey', textvariable=x1, font=5, width=15)
e1.place(x=100, y=1)

l2 =  Label(win, text='Number 2 ',font=5)
l2.place(x=1,y=30)
e2 = Entry(win, background='grey', textvariable=x2, font=5,width=15)
e2.place(x=100, y=30)

l3 =  Label(win, font=5)
l3.place(x=1,y=65)

sine = partial(sine, l3, x1)
cosine = partial(cosine, l3, x1)
tangent = partial(tangent, l3, x1)
mod = partial(mod, l3, x1)
add = partial(add, l3, x1, x2)
percent = partial(percent, l3, x1)
log = partial(log, l3, x1)
subtract = partial(subtract,l3,x1,x2)
mult = partial(mult, l3, x1, x2)
div = partial(div, l3, x1, x2)
power = partial(power, l3, x1, x2)
root = partial(root, l3, x1, x2)

add_button = Button(win, background='light green', text='+', height=2, width=4, font=3, command=add)
add_button.place(x=30, y=100)

sub_button = Button(win, background='light green', text='-', height=2, width=4,  font=3, command=subtract)
sub_button.place(x=90, y=100)

mul_button = Button(win, background='light green', text='*', height=2, width=4,  font=3, command=mult)
mul_button.place(x=150, y=100)

div_button = Button(win, background='light green', text='/', height=2, width=4,  font=3, command=div)
div_button.place(x=210, y=100)

per_button = Button(win, background='light green', text='%', height=2, width=4,  font=3, command=percent)
per_button.place(x=30, y=170)

log_button = Button(win, background='light green', text='log', height=2, width=4, font=3, command=log)
log_button.place(x=90, y=170)

pow_button = Button(win, background='light green', text='x^y', height=2, width=4,  font=3, command=power)
pow_button.place(x=150, y=170)

root_button = Button(win, background='light green', text='x^1/y', height=2, width=4,  font=3, command=root)
root_button.place(x=210, y=170)

sin_button = Button(win, background='light green', text='sin', height=2, width=4,  font=3, command=sine)
sin_button.place(x=30, y=240)

cos_button = Button(win, background='light green', text='cos', height=2, width=4, font=3, command=cosine)
cos_button.place(x=90, y=240)

tan_button = Button(win, background='light green', text='tan', height=2, width=4,  font=3, command=tangent)
tan_button.place(x=150, y=240)

mod_button = Button(win, background='light green', text='|x|', height=2, width=4,  font=3, bd=3, command=mod)
mod_button.place(x=210, y=240)



win.mainloop()