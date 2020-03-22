'''
tkinter_calculator.py

Created by Matthew Grunauer
3/22/2020

A simple calculator with limited functionality, built using the Tkinter library
'''

from tkinter import *

'''
Sets up the window for the calculator
'''
window = Tk()

window.title("Calculator")
window.geometry('300x265')
window.resizable(width=False, height=False)
window.configure(bg="LightGray")

top_frame = Frame(window)
top_frame.pack()
first_row = Frame(window)
first_row.pack()
second_row = Frame(window)
second_row.pack()
third_row = Frame(window)
third_row.pack()
fourth_row = Frame(window)
fourth_row.pack()

txt_1 = Text(top_frame, width=30, height=5)
txt_1.configure(bg="LightBlue")
txt_1.config(state=DISABLED)
txt_1.pack()
lbl_1 = Label(top_frame, text="")
lbl_1.pack()

# Global Variables
'''
one_operation makes sure that only one operation is being used per calculation
full_operation stores the contents of the operation
'''
one_operation = False
full_operation = ''

# Number Button Functions
'''
Each function checks to make sure that either the Text widget is empty
or that 0 is not the first number in the widget. This ensures numbers cannot be inputed as '09' or even '00'
NOTE: The Text widget must be enabled and disabled each time text is inserted into it to ensure a user cannot type their own
inputs into the widget
'''

def clicked_btn_1():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "1")
    else:
        txt_1.insert('end', "1")
    txt_1.config(state=DISABLED)
def clicked_btn_2():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "2")
    else:
        txt_1.insert('end', "2")
    txt_1.config(state=DISABLED)
def clicked_btn_3():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "3")
    else:
        txt_1.insert('end', "3")
    txt_1.config(state=DISABLED)
def clicked_btn_4():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "4")
    else:
        txt_1.insert('end', "4")
    txt_1.config(state=DISABLED)
def clicked_btn_5():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "5")
    else:
        txt_1.insert('end', "5")
    txt_1.config(state=DISABLED)
def clicked_btn_6():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "6")
    else:
        txt_1.insert('end', "6")
    txt_1.config(state=DISABLED)
def clicked_btn_7():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "7")
    else:
        txt_1.insert('end', "7")
    txt_1.config(state=DISABLED)
def clicked_btn_8():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "8")
    else:
        txt_1.insert('end', "8")
    txt_1.config(state=DISABLED)
def clicked_btn_9():
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:    
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "9")
    else:
        txt_1.insert('end', "9")
    txt_1.config(state=DISABLED)
def clicked_btn_0():
    checker = txt_1.get("1.0","end")
    txt_1.config(state=NORMAL)
    if len(txt_1.get('1.0','end')) > 1:
        if txt_1.get('1.0','end').rstrip()[0] != "0":
            txt_1.insert('end', "0")
    else:
        txt_1.insert('end', "0")
    txt_1.config(state=DISABLED)

# Operation Functions
'''
Each operation is stored as a function in a dictionary
'''
def addition(first_number, second_number):
    return first_number + second_number
def subtraction(first_number, second_number):
    return first_number - second_number
def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number, second_number):
    try:
        return first_number / second_number
    except:
        return "ERROR"

operations = {"+" : addition, "-" : subtraction, "*" : multiplication, "/" : division}

# Operation Button Functions
'''
Each button for each operation functions essentially the same with the exception of clicked_clear and clicked_equals.
Text widget must be enabled and disabled just as before.
'''
def clicked_add():
    global full_operation, one_operation
    txt_1.config(state=NORMAL)
    checker = txt_1.get("1.0","end")
    if one_operation == False and len(checker) > 1:
        full_operation += txt_1.get('1.0', END).rstrip()
        full_operation += " + "
        txt_1.delete('1.0', 'end')
        one_operation = True
        print(full_operation)
    txt_1.config(state=DISABLED)
        
def clicked_subtract():
    txt_1.config(state=NORMAL)
    global full_operation, one_operation
    checker = txt_1.get("1.0","end")
    if one_operation == False and len(checker) > 1:
        full_operation += txt_1.get('1.0', END).rstrip()
        full_operation += " - "
        txt_1.delete('1.0', 'end')
        one_operation = True
        print(full_operation)
    txt_1.config(state=DISABLED)
        
def clicked_multiply():
    global full_operation, one_operation
    txt_1.config(state=NORMAL)
    checker = txt_1.get("1.0","end")
    if one_operation == False and len(checker) > 1:
        full_operation += txt_1.get('1.0', END).rstrip()
        full_operation += " * "
        txt_1.delete('1.0', 'end')
        one_operation = True
        print(full_operation)
    txt_1.config(state=DISABLED)
        
def clicked_divide():
    global full_operation, one_operation
    txt_1.config(state=NORMAL)
    checker = txt_1.get("1.0","end")
    if one_operation == False and len(checker) > 1:
        full_operation += txt_1.get('1.0', END).rstrip()
        full_operation += " / "
        txt_1.delete('1.0', 'end')
        one_operation = True
        print(full_operation)
    txt_1.config(state=DISABLED)
        
def clicked_equals():
    global one_operation, full_operation, operations
    txt_1.config(state=NORMAL)
    if one_operation:
        full_operation += txt_1.get("1.0", 'end').rstrip()
        txt_1.delete('1.0','end')
        operation = full_operation.split(' ')
        first_number = float(operation[0])
        second_number = float(operation[2])
        operand = operation[1]
        for i in ['+','-','*','/']:
            if operand == i:
                lbl_1.configure(text=str(operations[i](first_number, second_number)))
        one_operation = False
        full_operation = ""
    txt_1.config(state=DISABLED)
        
def clicked_clear():
    global one_operation
    txt_1.config(state=NORMAL)
    txt_1.delete('1.0','end')
    lbl_1.configure(text='')
    txt_1.config(state=DISABLED)
    one_operation = False
    

# Setup Buttons For Functionality
'''
Buttons 0-9 and all the operations are setup here with their respective configurations
'''

btn_1 = Button(first_row, text="1", height=1, width=5, command=clicked_btn_1)
btn_1.pack(side=LEFT)
btn_2 = Button(first_row, text="2", height=1, width=5, command=clicked_btn_2)
btn_2.pack(side=LEFT)
btn_3 = Button(first_row, text="3", height=1, width=5, command=clicked_btn_3)
btn_3.pack(side=LEFT)
btn_add = Button(first_row, text="+", height=1, width=5, bg="LightGreen", command=clicked_add)
btn_add.pack(side=LEFT)
btn_subtract = Button(first_row, text="-", height=1, width=5, bg="Pink", command=clicked_subtract)
btn_subtract.pack(side=LEFT)
btn_4 = Button(second_row, text="4", height=1, width=5, command=clicked_btn_4)
btn_4.pack(side=LEFT)
btn_5 = Button(second_row, text="5", height=1, width=5, command=clicked_btn_5)
btn_5.pack(side=LEFT)
btn_6 = Button(second_row, text="6", height=1, width=5, command=clicked_btn_6)
btn_6.pack(side=LEFT)
btn_multiply = Button(second_row, text="*", height=1, width=5, bg="Yellow", command=clicked_multiply)
btn_multiply.pack(side=LEFT)
btn_divide = Button(second_row, text="/", height=1, width=5, bg="Orange", command=clicked_divide)
btn_divide.pack(side=LEFT)
btn_7 = Button(third_row, text="7", height=1, width=5, command=clicked_btn_7)
btn_7.pack(side=LEFT)
btn_8 = Button(third_row, text="8", height=1, width=5, command=clicked_btn_8)
btn_8.pack(side=LEFT)
btn_9 = Button(third_row, text="9", height=1, width=5, command=clicked_btn_9)
btn_9.pack(side=LEFT)
btn_clear = Button(third_row, text="CLEAR", height=1, width=5, bg="Cyan", command=clicked_clear)
btn_clear.pack(side=LEFT)
btn_0 = Button(fourth_row, text="0", height=1, width=5, command=clicked_btn_0)
btn_0.pack(side=LEFT)
btn_equals = Button(third_row, text="=", height=1, width=5, bg='Sienna', command=clicked_equals)
btn_equals.pack(side=LEFT)


# Opens the calculator interface

window.mainloop()
