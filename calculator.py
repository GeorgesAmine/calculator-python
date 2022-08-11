 
from tkinter import Button, PhotoImage, Text, Tk, font

# create calcuation string 
calculation = ""

# method that adds to calculation string when buttons are pressed
def  add_to_calculation(symbol):
    global calculation
    # add passed symbol to calculation and display it 
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that implements the backspace functionality
def erase_from_calculation():
    global calculation
    # erase last charachter from calculation and display the result 
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that evaluates the calculation string
def evaluate_calculation():
    global calculation
    try:
        # evaluate calculation using native eval() function
        # and diplay results
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        # in case of error clear the field and display error
        clear_field()
        text_result.insert(1.0, "Error")

# method that does the inverse when inverse button is pressed
def inverse():
    global calculation
    # inverse the evaluated calculation and display the result
    calculation = str(1/eval(calculation))
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# method that clears the field and initatize calculation string to ""
def clear_field():
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
virtualPixel = PhotoImage(width = 1, height = 1)

# buttons styling
btn_size = 38
btn_font = font.Font(size = 20)
num_btn_color = "#F2FBFF"
op_btn_color = "#D5E0ED"

# 1st row: display text fieldrow
text_result = Text(window, bg = "#F0F5FC", height = 3, width = 33)
text_result.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

# 2nd row
back_space = Button(window, command = erase_from_calculation, text = "\u2190",
                    bg = op_btn_color, height = btn_size, width = btn_size,
                    image = virtualPixel, compound = "c", font = btn_font)
back_space.grid(row = 1, column = 0, padx = 5, pady = 5)

clear_display = Button(window, command = clear_field, text = "C",
                       bg = op_btn_color, height = btn_size, width = btn_size,
                       image = virtualPixel, compound = "c", font = btn_font)
clear_display.grid(row = 1, column = 1, padx = 5, pady = 5)

left_par = Button(window, command = lambda:add_to_calculation("("), text = "(",
                  bg = op_btn_color, height = btn_size, width = btn_size,
                  image = virtualPixel, compound = "c", font = btn_font)
left_par.grid(row = 1, column = 2, padx = 5, pady = 5)

right_par = Button(window, command = lambda:add_to_calculation(")"), text = ")",
                   bg = op_btn_color, height = btn_size, width = btn_size,
                   image = virtualPixel, compound = "c", font = btn_font)
right_par.grid(row = 1, column = 3, padx = 5, pady = 5)

# numbers pad
num7 = Button(window, command = lambda:add_to_calculation(7), text = "7",
              bg = num_btn_color, height = btn_size, width = btn_size, 
              image = virtualPixel, compound = "c", font = btn_font)
num7.grid(row = 2, column = 0, padx = 5, pady = 5)

num8 = Button(window, command = lambda:add_to_calculation(8), text = "8",
              bg = num_btn_color, height = btn_size, width = btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num8.grid(row = 2, column = 1, padx = 5, pady = 5)

num9 = Button(window, command = lambda:add_to_calculation(9), text = "9",
              bg = num_btn_color, height = btn_size, width = btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num9.grid(row = 2, column = 2, padx = 5, pady = 5)

num4 = Button(window, command = lambda:add_to_calculation(4), text = "4",
              bg = num_btn_color, height = btn_size, width = btn_size, 
              image = virtualPixel, compound = "c", font = btn_font)
num4.grid(row = 3, column = 0, padx = 5, pady = 5)

num5 = Button(window, command = lambda:add_to_calculation(5), text = "5",
              bg = num_btn_color, height = btn_size, width = btn_size, 
              image = virtualPixel, compound = "c", font = btn_font)
num5.grid(row = 3, column = 1, padx = 5, pady = 5)

num6 = Button(window, command = lambda:add_to_calculation(6), text = "6",
              bg = num_btn_color, height = btn_size, width = btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num6.grid(row = 3, column = 2, padx = 5, pady = 5)

num1 = Button(window, command = lambda:add_to_calculation(1), text = "1",
              bg = num_btn_color, height = btn_size, width = btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num1.grid(row = 4, column = 0, padx = 5, pady = 5)

num2 = Button(window, command = lambda:add_to_calculation(2), text = "2",
              bg = num_btn_color, height = btn_size, width = btn_size, 
              image = virtualPixel, compound = "c", font = btn_font)
num2.grid(row = 4, column = 1, padx = 5, pady = 5)

num3 = Button(window, command = lambda:add_to_calculation(3), text = "3",
              bg = num_btn_color, height = btn_size, width = btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num3.grid(row = 4, column = 2, padx = 5, pady = 5)

num0 = Button(window, command = lambda:add_to_calculation(0), text = "0",
              bg = num_btn_color, height = btn_size, width = 2.5*btn_size,
              image = virtualPixel, compound = "c", font = btn_font)
num0.grid(row = 5, column = 0,columnspan=2, padx = 5, pady = 5)

comma = Button(window, command = lambda:add_to_calculation("."), text = ".",
               bg = num_btn_color, height = btn_size, width = btn_size,
               image = virtualPixel, compound = "c", font = btn_font)
comma.grid(row = 5, column = 2, padx = 5, pady = 5)

# operations
div_op = Button(window, command = lambda:add_to_calculation("/"), text = "/",
                bg = op_btn_color, height = btn_size, width = btn_size,
                image = virtualPixel, compound = "c", font = btn_font)
div_op.grid(row = 2, column = 3, padx = 5, pady = 5)

mult_op = Button(window, command = lambda:add_to_calculation("*"), text = "*",
                 bg = op_btn_color, height = btn_size, width = btn_size,
                 image = virtualPixel, compound = "c", font = btn_font)
mult_op.grid(row = 3, column = 3, padx = 5, pady = 5)

plus_op = Button(window, command = lambda:add_to_calculation("+"), text = "+",
                 bg = op_btn_color, height = btn_size, width = btn_size,
                 image = virtualPixel, compound = "c", font = btn_font)
plus_op.grid(row = 4, column = 3, padx = 5, pady = 5)

minus_op = Button(window, command = lambda:add_to_calculation("-"), text = "-",
                  bg = op_btn_color, height = btn_size, width = btn_size, 
                  image = virtualPixel, compound = "c", font = btn_font)
minus_op.grid(row = 5, column = 3, padx = 5, pady = 5)

# advanced operations
sqrt_op = Button(window, command = lambda:add_to_calculation("sqrt"), text = "\u221A",
                 bg = op_btn_color, height = btn_size, width = btn_size, 
                 image = virtualPixel, compound = "c", font = btn_font)
sqrt_op.grid(row = 1, column = 4, padx = 5, pady = 5)

modulo_op = Button(window, command = lambda:add_to_calculation("%"), text = "%",
                   bg = op_btn_color, height = btn_size, width = btn_size, 
                   image = virtualPixel, compound = "c", font = btn_font)
modulo_op.grid(row = 2, column = 4, padx = 5, pady = 5)

inverse_op = Button(window, command = inverse, text = "1/x", bg = op_btn_color,
                     height = btn_size, width = btn_size, image = virtualPixel,
                     compound = "c", font = btn_font)
inverse_op.grid(row = 3, column = 4, padx = 5, pady = 5)

# equal sign
equal = Button(window, command = evaluate_calculation, text = "=",
               bg = op_btn_color,  height = 2.48*btn_size, width = btn_size,
               image = virtualPixel, compound = "c", font = btn_font)
equal.grid(row = 4, column = 4, rowspan = 2, padx = 5, pady = 5)

window.mainloop()