from tkinter import *
import tkinter
from tkinter import font
from unittest import result
import numpy as np

calculation = ""
def  add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calculation)

def erase_from_calculation():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

window = Tk()
window.geometry("280x360")
window.title("Calculator")

virtualPixel = PhotoImage(width=1, height=1)
btn_size = 38
btn_font = font.Font(size=20)

# 1st row
text_result = Text(window,bg="white",height=3,width=33)
text_result.grid(row=0,column=0,columnspan=5,padx=5,pady=5)


# 2nd row
back_space = Button(window,command=erase_from_calculation,text="\u2190",bg="red",height=btn_size,width=btn_size,image=virtualPixel,compound="c",font=btn_font)
back_space.grid(row=1,column=0,padx=5,pady=5)

clear_display = Button(window,command=clear_field, text="CD",bg="red",height=btn_size,width=btn_size,image=virtualPixel,compound="c",font=btn_font)
clear_display.grid(row=1,column=1,padx=5,pady=5)

left_par = Button(window, command=lambda:add_to_calculation("("),text="(",bg="red",height=btn_size,width=btn_size,image=virtualPixel,compound="c",font=btn_font)
left_par.grid(row=1,column=2,padx=5,pady=5)

right_par = Button(window,command=lambda:add_to_calculation(")"), text=")",bg="red",height=btn_size,width=btn_size,image=virtualPixel,compound="c",font=btn_font)
right_par.grid(row=1,column=3,padx=5,pady=5)

# numbers pad
num7 = Button(window, command=lambda:add_to_calculation(7),text="7",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num7.grid(row=2,column=0,padx=5,pady=5)

num8 = Button(window, command=lambda:add_to_calculation(8), text="8",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num8.grid(row=2,column=1,padx=5,pady=5)

num9 = Button(window, command=lambda:add_to_calculation(9), text="9",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num9.grid(row=2,column=2,padx=5,pady=5)

num4 = Button(window, command=lambda:add_to_calculation(4), text="4",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num4.grid(row=3,column=0,padx=5,pady=5)

num5 = Button(window, command=lambda:add_to_calculation(5), text="5",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num5.grid(row=3,column=1,padx=5,pady=5)

num6 = Button(window, command=lambda:add_to_calculation(6), text="6",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num6.grid(row=3,column=2,padx=5,pady=5)

num1 = Button(window, command=lambda:add_to_calculation(1), text="1",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num1.grid(row=4,column=0,padx=5,pady=5)

num2 = Button(window, command=lambda:add_to_calculation(2), text="2",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num2.grid(row=4,column=1,padx=5,pady=5)

num3 = Button(window, command=lambda:add_to_calculation(3), text="3",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
num3.grid(row=4,column=2,padx=5,pady=5)

num0 = Button(window, command=lambda:add_to_calculation(0), text="0",bg="red",height=btn_size,width=2.5*btn_size, image=virtualPixel,compound="c",font=btn_font)
num0.grid(row=5,column=0,columnspan=2, padx=5,pady=5)

comma = Button(window,command=lambda:add_to_calculation("."), text=".",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
comma.grid(row=5,column=2,padx=5,pady=5)

# operations
div_op = Button(window,command=lambda:add_to_calculation("/"), text="/",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
div_op.grid(row=2,column=3,padx=5,pady=5)

mult_op = Button(window,command=lambda:add_to_calculation("*"), text="*",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
mult_op.grid(row=3,column=3,padx=5,pady=5)

plus_op = Button(window,command=lambda:add_to_calculation("+"), text="+",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
plus_op.grid(row=4,column=3,padx=5,pady=5)

minus_op = Button(window,command=lambda:add_to_calculation("-"), text="-",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
minus_op.grid(row=5,column=3,padx=5,pady=5)

# advanced operations
sqrt_op = Button(window,text="\u221A",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
sqrt_op.grid(row=1,column=4,padx=5,pady=5)

modulo_op = Button(window,text="%",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
modulo_op.grid(row=2,column=4,padx=5,pady=5)

inverse_op = Button(window,text="1/x",bg="red",height=btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
inverse_op.grid(row=3,column=4,padx=5,pady=5)

# equal
equal = Button(window,command=evaluate_calculation,text="=",bg="red",height=2.48*btn_size,width=btn_size, image=virtualPixel,compound="c",font=btn_font)
equal.grid(row=4,column=4,rowspan=2, padx=5,pady=5)

window.mainloop()