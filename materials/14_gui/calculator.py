from tkinter import *


gui = Tk()
gui.wm_title("simple calculator")

equation = StringVar()
entry = Entry(gui, width=35, borderwidth=5, textvariable=equation)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
equation.set("Enter the expression")
entry = ""


def on_click(value):
    global entry
    entry += str(value)
    equation.set(entry)


def equal():
    global entry
    total = str(eval(entry))
    equation.set(total)
    expression = ""


def clear():
    global entry
    entry = ""
    equation.set("")


button_1 = Button(gui, text="1", padx=30, pady=10, command=lambda: on_click(1))
button_2 = Button(gui, text="2", padx=30, pady=10, command=lambda: on_click(2))
button_3 = Button(gui, text="3", padx=30, pady=10, command=lambda: on_click(3))
button_add = Button(gui, text="+", padx=34,
                    pady=10, command=lambda: on_click("+"))

button_4 = Button(gui, text="4", padx=30, pady=10, command=lambda: on_click(4))
button_5 = Button(gui, text="5", padx=30, pady=10, command=lambda: on_click(5))
button_6 = Button(gui, text="6", padx=30, pady=10, command=lambda: on_click(6))
button_sub = Button(gui, text="-", padx=34,
                    pady=10, command=lambda: on_click("-"))

button_7 = Button(gui, text="7", padx=30, pady=10, command=lambda: on_click(7))
button_8 = Button(gui, text="8", padx=30, pady=10, command=lambda: on_click(8))
button_9 = Button(gui, text="9", padx=30, pady=10, command=lambda: on_click(9))
button_mul = Button(gui, text="*", padx=34,
                    pady=10, command=lambda: on_click("*"))

button_0 = Button(gui, text="0", padx=30, pady=10, command=lambda: on_click(0))
button_cls = Button(gui, text="CE", padx=26, pady=10, command=clear)
button_eql = Button(gui, text="=", padx=30, pady=10, command=equal)
button_div = Button(gui, text="/", padx=34,
                    pady=10, command=lambda: on_click("/"))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_div.grid(row=4, column=1)
button_cls.grid(row=4, column=2)
button_eql.grid(row=4, column=3)

gui.mainloop()
