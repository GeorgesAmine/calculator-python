"""
This program is a simple calculator GUI made with tkinter as
a clone to windows own calculator app
"""
from tkinter import Button, PhotoImage, Text, Tk, font

# create calcuation string
calculation = ""

# method that adds to calculation string when buttons are pressed
def  add_to_calculation(symbol):
    """
    adds a symbol to calculation string
    """
    global calculation
    # add passed symbol to calculation and display it
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that implements the backspace functionality
def erase_from_calculation():
    """
    Erases last char from calculation string
    """
    global calculation
    # erase last charachter from calculation and display the result
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that evaluates the calculation string
def evaluate_calculation():
    """"
    Evaluates calculation string
    """
    global calculation
    try:
        # evaluate calculation using native eval() function
        # and diplay results
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except ZeroDivisionError:
        # in case of error clear the field and display error
        clear_field()
        text_result.insert(1.0, "Error")

# method that does the inverse when inverse button is pressed
def inverse():
    """
    Calculates the inverse of a number
    """
    global calculation
    # inverse the evaluated calculation and display the result
    calculation = str(1/eval(calculation))
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that clears the field and initatize calculation string to ""
def clear_field():
    """
    Clear the field
    """
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# setup of Tk window
window = Tk()
window.geometry("280x360")
window.title("Calculator")
window.config(background = "#D9E4F1")

# create 1x1 image to pass to buttons in order to convert widths and
# heights to px
VIRTUAL_PIXEL = PhotoImage(width = 1, height = 1)

# buttons styling
BUTTON_SIZE = 38
BUTTON_FONT = font.Font(size = 20)
NUMBER_BUTTON_COLOR = "#F2FBFF"
OPERATION_BUTTON_COLOR = "#D5E0ED"

# 1st row: display text fieldrow
text_result = Text(window, bg = "#F0F5FC", height = 3, width = 33)
text_result.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

# 2nd row
back_space = Button(window, command = erase_from_calculation, text = "\u2190",
                    bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                    image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
back_space.grid(row = 1, column = 0, padx = 5, pady = 5)

clear_display = Button(window, command = clear_field, text = "C",
                       bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                       image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
clear_display.grid(row = 1, column = 1, padx = 5, pady = 5)

left_par = Button(window, command = lambda:add_to_calculation("("), text = "(",
                  bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                  image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
left_par.grid(row = 1, column = 2, padx = 5, pady = 5)

right_par = Button(window, command = lambda:add_to_calculation(")"), text = ")",
                   bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                   image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
right_par.grid(row = 1, column = 3, padx = 5, pady = 5)

# numbers pad
num7 = Button(window, command = lambda:add_to_calculation(7), text = "7",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num7.grid(row = 2, column = 0, padx = 5, pady = 5)

num8 = Button(window, command = lambda:add_to_calculation(8), text = "8",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num8.grid(row = 2, column = 1, padx = 5, pady = 5)

num9 = Button(window, command = lambda:add_to_calculation(9), text = "9",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num9.grid(row = 2, column = 2, padx = 5, pady = 5)

num4 = Button(window, command = lambda:add_to_calculation(4), text = "4",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num4.grid(row = 3, column = 0, padx = 5, pady = 5)

num5 = Button(window, command = lambda:add_to_calculation(5), text = "5",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num5.grid(row = 3, column = 1, padx = 5, pady = 5)

num6 = Button(window, command = lambda:add_to_calculation(6), text = "6",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num6.grid(row = 3, column = 2, padx = 5, pady = 5)

num1 = Button(window, command = lambda:add_to_calculation(1), text = "1",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num1.grid(row = 4, column = 0, padx = 5, pady = 5)

num2 = Button(window, command = lambda:add_to_calculation(2), text = "2",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num2.grid(row = 4, column = 1, padx = 5, pady = 5)

num3 = Button(window, command = lambda:add_to_calculation(3), text = "3",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num3.grid(row = 4, column = 2, padx = 5, pady = 5)

num0 = Button(window, command = lambda:add_to_calculation(0), text = "0",
              bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = 2.5*BUTTON_SIZE,
              image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
num0.grid(row = 5, column = 0,columnspan=2, padx = 5, pady = 5)

comma = Button(window, command = lambda:add_to_calculation("."), text = ".",
               bg = NUMBER_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
               image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
comma.grid(row = 5, column = 2, padx = 5, pady = 5)

# operations
div_op = Button(window, command = lambda:add_to_calculation("/"), text = "/",
                bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
div_op.grid(row = 2, column = 3, padx = 5, pady = 5)

mult_op = Button(window, command = lambda:add_to_calculation("*"), text = "*",
                 bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                 image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
mult_op.grid(row = 3, column = 3, padx = 5, pady = 5)

plus_op = Button(window, command = lambda:add_to_calculation("+"), text = "+",
                 bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                 image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
plus_op.grid(row = 4, column = 3, padx = 5, pady = 5)

minus_op = Button(window, command = lambda:add_to_calculation("-"), text = "-",
                  bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                  image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
minus_op.grid(row = 5, column = 3, padx = 5, pady = 5)

# advanced operations
sqrt_op = Button(window, command = lambda:add_to_calculation("sqrt"), text = "\u221A",
                 bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                 image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
sqrt_op.grid(row = 1, column = 4, padx = 5, pady = 5)

modulo_op = Button(window, command = lambda:add_to_calculation("%"), text = "%",
                   bg = OPERATION_BUTTON_COLOR, height = BUTTON_SIZE, width = BUTTON_SIZE,
                   image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
modulo_op.grid(row = 2, column = 4, padx = 5, pady = 5)

inverse_op = Button(window, command = inverse, text = "1/x", bg = OPERATION_BUTTON_COLOR,
                     height = BUTTON_SIZE, width = BUTTON_SIZE, image = VIRTUAL_PIXEL,
                     compound = "c", font = BUTTON_FONT)
inverse_op.grid(row = 3, column = 4, padx = 5, pady = 5)

# equal sign
equal = Button(window, command = evaluate_calculation, text = "=",
               bg = OPERATION_BUTTON_COLOR,  height = 2.48*BUTTON_SIZE, width = BUTTON_SIZE,
               image = VIRTUAL_PIXEL, compound = "c", font = BUTTON_FONT)
equal.grid(row = 4, column = 4, rowspan = 2, padx = 5, pady = 5)

window.mainloop()
