import os
import time
import random

# from IPython.display import clear_output

class Clovek:
    mod_zdravi = 10   # celkove zdravi = zivoty * mod_zdravi
    mod_energie = 5   # clovek=prumer; bojovnik +1; kouzelnik -1
    mod_moudrost = 1  # clovek=prumer; bojovnik -1; kouzelnik +1


class Bojovnik(Clovek):
    def __init__(self, jmeno, sila, zivoty):
        self.sila = sila
        self.jmeno = jmeno
        self.energie = self.mod_energie - 1  # postih bojovniku
        self.max_zivoty = self.zdravi(zivoty)
        self.akt_zivoty = self.max_zivoty
        self.moudrost = self.mod_moudrost - 1  # postih bojovniku

    def pozdrav(self):
        return f"{self.jmeno.upper()}: Ahoj, jsem bojovnik!"

    def zdravi(self, zivoty):
        return self.mod_zdravi * zivoty

    @classmethod
    def vytvor_instanci(cls):
        return cls("Arnold", 40, 10)


class Kouzelnik(Clovek):
    def __init__(self, jmeno, sila, zivoty):
        self.jmeno = jmeno
        self.sila = sila
        self.energie = self.mod_energie + 1  # zlepseni kouzelnika
        self.max_zivoty = self.zdravi(zivoty)
        self.akt_zivoty = self.max_zivoty
        self.moudrost = self.mod_moudrost + 1  # zlepseni kouzelnika

    def pozdrav(self):
        return f"{self.jmeno.upper()}: Ahoj, jsem kouzelnik!"

    def zdravi(self, zivoty):
        return self.mod_zdravi * zivoty


    @classmethod
    def vytvor_instanci(cls):
        return cls("Matous", 20, 7)

bojovnik_1 = Bojovnik.vytvor_instanci()
kouzelnik_1 = Kouzelnik.vytvor_instanci()

arena = [bojovnik_1, kouzelnik_1]

if bojovnik_1.moudrost > kouzelnik_1.moudrost:
    hrac_1 = bojovnik_1
    hrac_2 = kouzelnik_1
else:
    hrac_1 = kouzelnik_1
    hrac_2 = bojovnik_1


def utok_hrace(hrac):
    if isinstance(hrac, Bojovnik):
        return random.choice(range(hrac.sila + 1))
    else:
        return hrac.sila


def stav_boje(hrac_1, hrac_2, utok):
    os.system("clear")
    print(f"{hrac_1.jmeno} UTOCI ZA {utok}")
    print(f"{hrac_2.jmeno}: {hrac_2.akt_zivoty}/{hrac_2.max_zivoty}")
    time.sleep(2)


def zaverecna_obrazovka(vitez, porazeny, arena):
    import webbrowser
    url = "https://i.ytimg.com/vi/LrGPT8-64y0/maxresdefault.jpg"

    if vitez.jmeno == "Matous":
        webbrowser.open(url, 2)
        arena.remove(porazeny)
    else:
        arena.remove(porazeny)
        print(f"VYHRAVA: {vitez.jmeno}!")


while len(arena) == 2:
    utok = utok_hrace(hrac_1)  # 20
    hrac_2.akt_zivoty -= utok
    hrac_1.energie -= 1
    stav_boje(hrac_1, hrac_2, utok) # 2x print(), 4-sec delay

    if hrac_2.akt_zivoty <= 0:
        zaverecna_obrazovka(hrac_1, hrac_2, arena)
    elif hrac_1.energie == 0:
        zaverecna_obrazovka(hrac_2, hrac_1, arena)
    else:
        hrac_1, hrac_2 = hrac_2, hrac_1

