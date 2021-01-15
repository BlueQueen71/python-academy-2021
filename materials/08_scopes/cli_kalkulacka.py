import os


OPS = ("+", "-", "*", "/", "prum", "pow", "quit")


def umocneni():
    """
    Globalni prostredi vs. lokalni prostredi vs. built-in prostredi
    """
    x1 = input("hodnota:")
    x2 = input("mocnina:")
    return int(x1) ** int(x2)


def nabidka(*args):
    """
    Rozdil mezi aplikaci metody a funkce, doplnit
    """
    vyber = ' | '.join(*args)
    SEP = "-" * len(vyber)
    print(SEP, vyber, SEP, sep="\n")


def pocitani():
    celkem = "("
    while True:
        vstupek = input("tlacitko:")

        if vstupek.isnumeric():
            celkem += str(vstupek)
        elif vstupek in ("+", "-"):
            celkem += str(vstupek)
        elif vstupek in ("/", "*"):
            celkem += f"){vstupek}("
        elif vstupek == "=":
            celkem += ")" if celkem[:-1] != ")" else ""
            print(eval(celkem))
            break


def prumer():
    """
    Dokumentace funkci, teorie + ukazky
    """
    rada_cisel = list()
    while (vstupek := input("vstup")) != "quit":
        if vstupek.isnumeric():
            rada_cisel.append(int(vstupek))
        continue
    return sum(rada_cisel)/len(rada_cisel)


while True:
    """
    Pouziti parametru funkce -> args
    """
    nabidka(OPS)
    vyber = input("operace:")

    if vyber == "quit":
        print("ukoncuji")
        break
    elif vyber in ("+", "-", "*", "/"):
        pocitani()
    elif vyber == "prum":
        print(prumer())
    elif vyber == "pow":
        clear_output()
        print(umocneni())




