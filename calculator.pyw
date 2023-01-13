#Calculator_Prayaag_Munshi
#Creating a Calculator using Tkinter
#Programmer: P. Munshi
#Date: 6/4/21
#version: 1.0

from tkinter import *
from tkinter import messagebox
import math

button_texts = [[' C ', ' √ ', 'x^y', ' % '], [' 1 ', ' 2 ', ' 3 ', ' + '], [' 4 ', ' 5 ', ' 6 ', ' - '], [' 7 ',' 8 ',' 9 ' , ' * '],
                [' 0 ', ' . ', 'LOG', ' / '], [' ( ', ' ) ', ' \u220F ', ' = '], ['Del', 'X']]
max_row_size = max([len(array) for array in button_texts])
offset = 30
window_height = len(button_texts) * (offset + 10)
window_width = (max_row_size * (offset + 1)) + (2 * offset)

window = Tk()
window.resizable(False, False)
window.geometry("{0}x{1}".format(window_width, window_height))
window.title("")

calculator_output = Label(text = '', bg = "grey70")

def computeEquation(equation):
    equation = equation.strip().split()
    for i in range(len(equation)):
        if equation[i] == 'log(': equation[i] = 'math.log10('

        elif equation[i] == 'sqrt(': equation[i] = 'math.sqrt('

        elif equation[i] == '^': equation[i] = '**'

        elif equation[i] == ' 3.14159 ': equation[i] = 'math.pi'

    equation = ''.join(equation)
    try:
        return str(eval(equation))

    except ZeroDivisionError:
        messagebox.showerror("Input Error", "Can not Divide by 0.")
        calculator_output["text"] = ''

    except:    
        messagebox.showerror("Input Error", "Invalid Syntax")


        
def buttonClicked(button_text):
    if button_text == 'X': window.destroy()
    if (button_text == 'Del'):
        if calculator_output["text"] != "":
            calculator_output["text"] = calculator_output["text"][:-1] 
    elif button_text == ' = ': calculator_output["text"] = computeEquation(calculator_output["text"])
    elif button_text == ' C ': calculator_output["text"] = ''
    elif button_text == ' √ ': calculator_output["text"] += 'sqrt( '
    elif button_text == 'LOG': calculator_output["text"] += 'log( '
    elif button_text == 'x^y': calculator_output["text"] += ' ^ '
    elif button_text == ' \u220F ': calculator_output["text"] += ' 3.14159 '
    elif button_text ==' ) ': calculator_output["text"] += ') '
    elif button_text ==' ( ': calculator_output["text"] += ' ('
    elif button_text == ' . ': calculator_output["text"] += '.'
    else: 
        calculator_output["text"] += button_text

buttons = [[Button(text = j, bg = "SlateGray2", activebackground = "LightSkyBlue1") for j in i] for i in button_texts]
[[[i.configure(command = lambda: buttonClicked(i["text"])) for i in [btn]] for btn in array] for array in buttons]


calculator_output.place(x = offset, y = offset, width = (offset + 1) * len(buttons[0]))

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        buttons[i][j].place(x = j*(offset + 1) + offset, y = i*(offset + 1) + 50, height = offset, width = offset)


window.mainloop()