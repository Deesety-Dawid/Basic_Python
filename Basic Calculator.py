from tkinter import *
root = Tk()

eq_ua = ""

# Functions


def btn_press(num):
    global eq_ua
    eq_ua = eq_ua + str(num)
    equation.set(eq_ua)


def equal_press():
    global eq_ua
    total = eval(eq_ua)
    equation.set(total)
    eq_ua = ""


def clear_label():
    global eq_ua
    eq_ua = ""
    equation.set("")


equation = StringVar()
calculation = Label(root, textvariable=equation)

equation.set("Write your expression")
calculation.grid(columnspan=4)

# Buttons
one = Button(root, text='1', command=lambda: btn_press(1))
one.grid(row=1, column=0)

two = Button(root, text='2', command=lambda: btn_press(2))
two.grid(row=1, column=1)

three = Button(root, text='3', command=lambda: btn_press(3))
three.grid(row=1, column=2)

four = Button(root, text='4', command=lambda: btn_press(4))
four.grid(row=2, column=0)

five = Button(root, text='5', command=lambda: btn_press(5))
five.grid(row=2, column=1)

six = Button(root, text='6', command=lambda: btn_press(6))
six.grid(row=2, column=2)

seven = Button(root, text='7', command=lambda: btn_press(7))
seven.grid(row=3, column=0)

eight = Button(root, text='8', command=lambda: btn_press(8))
eight.grid(row=3, column=1)

nine = Button(root, text='9', command=lambda: btn_press(9))
nine.grid(row=3, column=2)

zero = Button(root, text='0', command=lambda: btn_press(0))
zero.grid(row=4, column=1)

# Operators
op_plus = Button(root, text="+", command=lambda: btn_press("+"))
op_plus.grid(row=1, column=3)

op_minus = Button(root, text="-", command=lambda: btn_press("-"))
op_minus.grid(row=2, column=3)

op_multiply = Button(root, text="*", command=lambda: btn_press("*"))
op_multiply.grid(row=3, column=3)

op_divide = Button(root, text="/", command=lambda: btn_press("/"))
op_divide.grid(row=4, column=3)

# Getting result
op_equal = Button(root, text="=", command=equal_press)
op_equal.grid(row=4, column=2)

op_clear = Button(root, text="C", command=clear_label)
op_clear.grid(row=4, column=0)

root.mainloop()
