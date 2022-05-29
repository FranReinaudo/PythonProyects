from tkinter import *

def button_press(num):
    global equation
    equation = equation + str(num)
    equation_label.set(equation)

def equal():
    global equation
    try:
        equation_label.set(str(eval(equation)))
        equation = str(eval(equation))
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation = ""
    except SyntaxError:
        equation_label.set("syntax error")
        equation = ""


def clear():
    global equation
    equation_label.set("")
    equation = ""

window = Tk()

window.title("Calculator")
window.geometry("600x600")

equation = ""
equation_label = StringVar()

display = Label(window, textvariable=equation_label, bg="white", width=30, height=2, font=("Consolas", 20))
display.pack()

BUTTON_WIDTH = 7
BUTTON_HEIGHT = 3

frame = Frame(window)
frame.pack()

button1 = Button(frame, command=lambda: button_press(1), font=("Consolas", 20), text=1, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button1.grid(column=0, row=0)

button2 = Button(frame, command=lambda: button_press(2), font=("Consolas", 20), text=2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button2.grid(column=1, row=0)

button3 = Button(frame, command=lambda: button_press(3), font=("Consolas", 20), text=3, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button3.grid(column=2, row=0)

button4 = Button(frame, command=lambda: button_press(4), font=("Consolas", 20), text=4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button4.grid(column=0, row=1)

button5 = Button(frame, command=lambda: button_press(5), font=("Consolas", 20), text=5, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button5.grid(column=1, row=1)

button6 = Button(frame, command=lambda: button_press(6), font=("Consolas", 20), text=6, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button6.grid(column=2, row=1)

button7 = Button(frame, command=lambda: button_press(7), font=("Consolas", 20), text=7, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button7.grid(column=0, row=2)

button8 = Button(frame, command=lambda: button_press(8), font=("Consolas", 20), text=8, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button8.grid(column=1, row=2)

button9 = Button(frame, command=lambda: button_press(9), font=("Consolas", 20), text=9, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button9.grid(column=2, row=2)

button0 = Button(frame, command=lambda: button_press(0), font=("Consolas", 20), text=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button0.grid(column=0, row=3)

buttonDec = Button(frame, command=lambda: button_press("."), font=("Consolas", 20), text=".", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonDec.grid(column=1, row=3)

buttonEqual = Button(frame, command=equal, font=("Consolas", 20), text="=", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonEqual.grid(column=2, row=3)

buttonDiv = Button(frame, command=lambda: button_press("/"), font=("Consolas", 20), text="/", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonDiv.grid(column=4, row=0)

buttonMul = Button(frame, command=lambda: button_press("*"), font=("Consolas", 20), text="X", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonMul.grid(column=4, row=1)

buttonMinus = Button(frame, command=lambda: button_press("-"), font=("Consolas", 20), text="-", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonMinus.grid(column=4, row=2)

buttonPlus = Button(frame, command=lambda: button_press("+"), font=("Consolas", 20), text="+", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
buttonPlus.grid(column=4, row=3)

buttonClear = Button(window, command=clear, font=("Consolas", 20), text="Clear", width=12, height=BUTTON_HEIGHT)
buttonClear.pack()

window.mainloop()
