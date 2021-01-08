#!/usr/bin/python3
import os
from random import choice

import figurka

zivoty = 7
hra_bezi = True


def vytvor_tajenku() -> tuple:
    vyber_slov = ["obesenec", "autobus", "klavesnice", "nedele"]
    return (slovo := choice(vyber_slov), ["_"] * len(slovo))


def aktualni_stav_hry(tajenka: list, zivoty: int, beh_hry: bool) -> None:
    status = f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}"
    print(figurka.hangman.get(7 - zivoty), status, sep="\n")
    if not beh_hry and zivoty > 0:
        print("Vyhral jsi! Gratulace")
    elif zivoty == 0:
        print("Prohral jsi! Snad priste")


def aktualni_stav_hry(tajenka: list, zivoty: int, beh_hry: bool) -> None:
    os.system("clear")
    status = f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}"
    print(figurka.hangman.get(7 - zivoty), status, sep="\n")

    if not beh_hry and zivoty > 0:
        print("Vyhral jsi! Gratulace")
    elif zivoty == 0:
        print("Prohral jsi! Snad priste")


def zkontroluj_vybrane_pismeno(pismeno: str, slovo: str, tajenka: list) -> bool:
    for index, symbol in enumerate(slovo):
        if symbol == pismeno:
            tajenka[index] = pismeno

    return False if "_" not in tajenka else True


slovo, tajenka = vytvor_tajenku()  # TODO

while hra_bezi and zivoty > 0:
    aktualni_stav_hry(tajenka, zivoty, hra_bezi)  # TODO
    hadani = input("Hadej pismeno nebo cele slovo:")

    if hadani == slovo:
        hra_bezi = False

    elif len(hadani) == 1 and hadani in slovo:
        hra_bezi = zkontroluj_vybrane_pismeno(hadani, slovo, tajenka)  # TODO

    else:
        zivoty -= 1

aktualni_stav_hry(slovo, zivoty, hra_bezi)  # TODO

