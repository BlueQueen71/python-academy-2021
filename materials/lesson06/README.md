➡ [vratit se na patou lekci](https://github.com/Bralor/python-academy/tree/lekce05)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 6⃣ Python academy
### 🗒 Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Moduly & baliky
4. Importovani
5. Rozdeleni podle puvodu
---


### 🗒 Uzitecne odkazy
- [Neoficialni dokumentace prirazovaciho operatoru (realpython.com)](https://realpython.com/lessons/assignment-expressions/)
- [Standartni instalator balicku pro Python pip/pip3 (pypi.org)](https://pypi.org/project/pip/)
- [Hledani modulu pomoci interpretu Pythonu (python.org)](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
- [Neoficialni dokumentace o ucelu souboru \_\_init\_\_.py](https://pythontips.com/2013/07/28/what-is-__init__-py/)
- [Jak nainstalovat knihovny tretich stran pomoci Pycharm (jetbrains.com)](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)

---

### ⏯  Ukazka ulohy
<details>
  <summary>ℹ Pro vice informaci o spusteni ukazky kliknete na tento text</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **obesenec.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

### Uvod do hry
<details>
   <summary>💾 Uvod hry - uvodni promenne, potrebne pro prubeh hry _obesenec_ </summary>

   #### 🎮 Pocatecni promenne
   1. `SLOVO` obsahuje hadane slovo (konstanta)
   2. `tajenka` prepise jednotliva pismena na podtrzitka
   3. `zivoty` nastavime defaultni pocet pokusu jako `7`
   4. `hra_bezi` pomucka pro ukonceni prubehu hry (`True`)

<details>
   <summary>✍ Nas zapis</summary>

   #### 📂 obesenec.py
   ```python
   #!/usr/bin/python3

   SLOVO = "obesenec"            # libovolne slovo pro zkouseni
   tajenka = len(SLOVO) * ["_"]  # nelze pouzit string
   zivoty = 7
   hra_bezi = True
   ```
</details>

<!--PRVNI CAST HRY-->

---

</details>

<details>
   <summary>♻ Prubeh hry - proces, ktery se opakuje v kazdem kole hry</summary>

   #### 👀 V kazdem kole
   1. Vypsat stav hry
   2. Necham hrace zadat pismeno/slovo (promenna `hadani`)
   3. Sestavime vhodne podminky (uhodne slovo/ pismeno/ neuhodne)

<details>
   <summary>✍ Nase reseni</summary>

   #### 📂 obesenec.py
   ```python
   print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")
   hadani = input("Hadej pismeno nebo cele slovo:")

   if hadani == SLOVO:
       hra_bezi = False

   elif len(hadani) == 1 and hadani in SLOVO:
       print()

   else:
       zivoty -= 1
   ```
   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/sample1-1#main.py)

</details>

   #### 🔚 Game over!
   1. Pokud ma hrac v `zivoty = 0`
   2. Pokud `hra_bezi = False`

<details>
   <summary>✍ Nase reseni</summary>

   #### 📂 obesenec.py
   ```python
   while hra_probiha and zivoty > 0:
       print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")
       hadani = input("Hadej pismeno nebo cele slovo:")

       if hadani == SLOVO:
           hra_bezi = False

       elif len(hadani) == 1 and hadani in SLOVO:
           print()

       else:
           zivoty -= 1

   else:
       if not hra_probiha:
           print(f"Tajenka: {SLOVO}", "Jsi vitez hry, gratulace", sep="\n")
       else:
           print(f"Bohuzel, prohrals:(", f"Hledane slovo: *{SLOVO}*", sep="\n")
   ```
</details>

---

</details>

<details>
   <summary>🐂 Mozna upravy - pomoci externich knihoven muzeme hru zdokonalit </summary>

   #### 🔧 Co muzeme upravit
   1. Pridat ruzna hadana slova
   2. Zajistit nahodny vyber slova
   3. Vykreslit menici se figurku obesence v kazdem kole
   4. Zajistit cistejsi vypis

</details>

---

### Knihovny Pythonu

<details>
   <summary>📗 Moduly - standartni moduly jako soubory v Pythonu</summary>

   #### ☝ K zapamatovani
   1. Jde o soubor s priponou `py`
   2. Obsahuje promenne, datove typy, standartni algoritmy
   3. Nektere jiz mame k dispozici (napr. `usr/lib/python3.x/`)
   ```python
   import pprint


   UDAJE = {"jmeno": "Matous", "prijmeni": "Holinka", "email": "matous@matous.cz",
       "adresa": "Kocourkov, U Potoka 28"}

   pprint.pprint(UDAJE)
   ```
   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/module#main.py)

---

</details>

<details>
   <summary>🗃 Balik - standartni baliky jako adresare v Pythonu</summary>

   #### ☝ K zapamatovani
   1. Sbirka nekolika modulu
   2. Spolecne umistene v adresari
   3. Baliky obsahuji `__init__.py`
   4. Baliky obsahuji `__pycache__`

   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/myownpackage#main.py)

   #### 🔍 Soubor init
   Tento, dost casto prazdny, soubor umoznuje interpretu najit & nahrat moduly.
   **Pozor!** nemusi byt prazdny, nekdy obsahuje dokumentace, zavislosti, aj.

   #### ⏩ Slozka pycache
   Tato slozka vznika, kdyz spoustime kod a interpret jej zkompiluje
   na _bytecode_. Nasledne schova zkompilovany kod do tohoto adresare.

---

</details>

<details>
   <summary>⏪ Zaver - souhrn hlavnich bodu pro praci s knihovnami</summary>

   #### 💪 Souhrn vyhod modulu & baliku
   1. Nemusime opakovane prepisovat stejne instrukce
   2. Muzu opakovane pouzivat na vice mistech
   3. Citelnosti je ucineno zadost

</details>

</details>

---

### Proces importovani

<details>
   <summary>📥 Metody importovani - 3 zpusoby pro nahrani knihoven</summary>

   #### ☝ K zapamatovani
   1. `import pprint` - nahrajeme cely modul, pouziti `modul.funkce` (muzeme doplnit alias)
   2. `from pprint import *` - nahrajeme cely modul, pouziti `funkce`
   3. `from pprint import pprint` - nahraje pouze vybranou funkci (`funkce`) (muzeme doplnit alias)
   4. `as` - doplneni aliasu, pouziti `from pprint import pprint as pp` (`pp`)
   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/importingmethods#main.py)

---

</details>

<details>
   <summary>📽 Hledani modulu - proces hledani modulu pomoci interpretu</summary>

   #### ☝ K zapamatovani
   1. Interpret uvidi oznameni o nahravani modulu (pr. `import`)
   2. Prohleda zabudovane moduly: `sys.builtin_module_names`
   3. Dale prohleda: `sys.modules` (s podporou symlinku)
   4. Dale prohleda aktualni umisteni: `sys.path[0]` (pokud nejsou symlinky, bude 3.)
   5. Dale prohleda: `sys.path[1:]`
   6. Pokud **nenasel** -> `ModuleNotFound`
   7. Pokud **nasel** -> nahravam modul, prip. balik
   [**🔝 Vyzkousej sam 🔝**](https://repl.it/@JustBraloR/wrongway#main.py)

</details>

---

### Rozdeleni podle puvodu

<details>
   <summary>🏘 Knihovny standartn - mame ihned po instalaci k dispozici</summary>

   #### ☝ K zapamatovani
   Nainstalujeme jazyk, interpret a tyto knihovny. Nemusim instalovat, staci
   nahrat a pouzivat.

   #### ❓Modul random
   Pokud vyzadujeme vyuziti [prvku pseudo-nahody](https://docs.python.org/3/library/random.html),
   pouzijeme standartni modul `random`:

<details>
   <summary>✍ Nase reseni</summary>

   #### 📂obesenec.py
   ```python
   import random

   SLOVA = ["obesenec", "autobus", "klavesnice", "nedele"]
   slovo = random.choice(SLOVA)
   ```
---

</details>

   #### 🕺 Vlastni modul
   1. Spolecne si nahrajeme nas vlastni modul `figurka.py`
   2. Pouzijeme slovnik `hangman` uvnitr souboru
   3. Doplnime vypis v kazdem kole a pri prohre

<details>
   <summary>✍ Nase reseni</summary>

   #### 📂obesenec.py
   ```python
   import figurka

   print(figurka.hangman[7 - zivoty])
   ```
---

</details>

   #### 📺 Modul os
   1. Protoze je nase hra prilis upovidana, nahrajeme dalsi standartni modul,
   ktery nam pomuze udrzet vystup mene upovidany
   2. Aplikujeme funkci, pro strucny vystup ve vypisu a v zaveru

<details>
   <summary>✍ Nase reseni</summary>

   #### 📂obesenec.py
   ```python
   import os

   os.system("clear")  # win: os.system("cls")
   ```
</details>

---

</details>

<details>
   <summary>👾 Knihovny tretich stran</summary>

   Material je soucasti 12. lekce 😈

</details>

<!--PRIJDE DO POSLEDNI LEKCE
   #### ☝ K zapamatovani
   Protoze je knihoven pro Python spousta, nektere je potreba doinstalovat rucne.

<br />
<p align="center">
  <img alt="terminal-icon" width="80px" src="https://cubiclenate.files.wordpress.com/2018/04/terminal-icon.png?w=286&h=286" />
</p>

   #### 🆑 Pomoci prikazoveho radku
   1. Vytvorime virtualni pracovni prostredi:
   ```bash
   python3 -m venv <jmeno_prostredi>
   ```

   2. Aktivujeme virtualni pracovni prostredi:
   ```bash
   source <jmeno_prostredi>/bin/activate
   ```
   **Pozor!** Po aktivaci dostaneme na zacatku dotazovaciho radku zavorku
   se jmenem prostredi (pr. `(env)`)

   3. Overime dostupnost spravce balicku `pip3 --version`

   4. Pokud mame, instalujeme balicky (nahled [pypi.org](https://pypi.org/)):
   ```bash
   pip3 install <jmeno_balicku>         # instalace
   pip3 uninstall <jmeno_balicku>       # odstraneni
   pip3 --help                          # napoveda
   ```

   5. Vytvoreni souboru `requirements.txt` se zavislostmi:
   ```bash
   pip3 freeze > requirements.txt
   ```

   6. Pomoci zavilosti mohou ostatni uzivatele nainstalovat externi knihovny z 
   naseho virtualniho prostredi:
   ```bash
   pip3 install -r requirements.txt
   ```

<br />
<p align="center">
  <img alt="pycharm-icon" width="80px" src="https://caktus-website-production-2015.s3.amazonaws.com/media/blog-images/logo.png" />
</p>

   #### 🐍 Pomoci PyCharm
   1. Spustime Pycharm a otevreme projekt
   2. `ctrl + alt + s` -> Settings
   3. -> Project: <jmeno_projektu>
   4. -> Project interpreter
   5. ⚙ `Add...` Pridat prostredi/pouzit stavajici
   6. ➕ Instalovat knihovny pomoci symbolu `+` dole pod nabidkou
   7. `Terminal` dole na liste pro export zavislosti (`pip3 freeze > requirements.txt`)

</details>

</details>
-->
---

➡ [pokracovat k sedme lekci]()

