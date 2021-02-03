from tkinter import Tk, Button, Entry, StringVar


gui = Tk()
gui.geometry("550x310")
gui.wm_title("Kalkulator")

rovnice = StringVar()
vstup = Entry(gui, width=50, borderwidth=5, textvariable=rovnice)
vstup.grid(row=0, column=0, columnspan=4, ipadx=70)
rovnice.set("Zmacknete tlacitko s cislem")
zadani = ""  # 1 + 1...


def vypis(cislo):
    global zadani
    zadani += str(cislo)
    rovnice.set(zadani)


def vysledek():
    global zadani
    celkem = str(eval(zadani))
    rovnice.set(celkem)
    zadani = str(celkem)  # doplnit .ipynb-solution


def vycisti_zapis():
    global zadani
    zadani = ""
    rovnice.set("")


tlacitko_1 = Button(gui, text="1", width=10, pady= 20, command=lambda: vypis(1))
tlacitko_2 = Button(gui, text="2", width=10, pady= 20, command=lambda: vypis(2))
tlacitko_3 = Button(gui, text="3", width=10, pady= 20, command=lambda: vypis(3))
tlacitko_add = Button(gui, text="+", width=10, pady= 20, command=lambda: vypis("+"))

tlacitko_4 = Button(gui, text="4", width=10, pady= 20, command=lambda: vypis(4))
tlacitko_5 = Button(gui, text="5", width=10, pady= 20, command=lambda: vypis(5))
tlacitko_6 = Button(gui, text="6", width=10, pady= 20, command=lambda: vypis(6))
tlacitko_sub = Button(gui, text="-", width=10, pady= 20, command=lambda: vypis("-"))

tlacitko_7 = Button(gui, text="7", width=10, pady= 20, command=lambda: vypis(7))
tlacitko_8 = Button(gui, text="8", width=10, pady= 20, command=lambda: vypis(8))
tlacitko_9 = Button(gui, text="9", width=10, pady= 20, command=lambda: vypis(9))
tlacitko_mul = Button(gui, text="*", width=10, pady= 20, command=lambda: vypis("*"))

tlacitko_0 = Button(gui, text="0", width=10, pady= 20, command=lambda: vypis(0))
tlacitko_div = Button(gui, text="/", width=10, pady= 20, command=lambda: vypis("/"))
tlacitko_clr = Button(gui, text="CE", width=10, pady= 20, command=vycisti_zapis)
tlacitko_eql = Button(gui, text="=", width=10, pady= 20, command=vysledek)

tlacitko_1.grid(row=1, column=0)
tlacitko_2.grid(row=1, column=1)
tlacitko_3.grid(row=1, column=2)
tlacitko_add.grid(row=1, column=3)

tlacitko_4.grid(row=2, column=0)
tlacitko_5.grid(row=2, column=1)
tlacitko_6.grid(row=2, column=2)
tlacitko_sub.grid(row=2, column=3)

tlacitko_7.grid(row=3, column=0)
tlacitko_8.grid(row=3, column=1)
tlacitko_9.grid(row=3, column=2)
tlacitko_mul.grid(row=3, column=3)

tlacitko_0.grid(row=4, column=0)
tlacitko_div.grid(row=4, column=1)
tlacitko_clr.grid(row=4, column=2)
tlacitko_eql.grid(row=4, column=3)

gui.mainloop()
