➡ [vratit se k pate casti](https://github.com/Bralor/python-workshop/tree/master/materials/05_functions_and_text_files)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 6⃣ Python workshop
### 🗒  Obsah lekc
1. Uzitecne odkazy
2. Ukazka ulohy
3. Networking, pojmy
4. Server-klient, pripojeni
5. Server-klient, pokracovani
6. Server-klient, komunikace

---

<details>
  <summary>☝  Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkazy
  - [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
  - [Modul socket](https://docs.python.org/3/library/socket.html?highlight=socket#socket.socket.listen)

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/06_networking/server.py** v PyCharm
  3. 💅 Spustte soubor **materials/06_networking/client.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>🕸 Networking, pojmy</summary>

  #### 📥 Sockety
  Jsou to koncove body obousmerneho komunikacniho kanalu mezi klientem
  a serverem (napr. vas prohlizec a server). V networkingu je v podstate
  jednoznacnym identifikatorem v ramci cele site (ip adresa + cislo portu).

  #### ☄ TCP protokol
  - spojove orientovany na tok bajtu -> spolehlive dorucovani
  - ve spravnem poradi
  - umi rozdelit data pro vice aplikaci (web.server/email server na jednom pc)
  - obousmerny
  - `SOCK_STREAM` - nastaveni u modulu `socket` pro tcp protokol

  #### ♿ UDP protokol
  - je vhodny pro nasazeni pri male rezii nebo DNS
  - nezarucuje doruceni paketu oproti TCP
  - nezachovava poradi
  - `SOCK_DGRAM` - nastaveni u modulu `socket` pro udp protokol

  #### 🐍M odul socket
  1. Nejprve vytvorime objektovou reprezentaci socketu:
  ```python
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```
    - `socket.AF_INET` - argument stanovujici adresu typu ipv4 `100.50.200.5`
    - `socket.SOCK_STREAM` - argument reprezentujici typ socketu (TCP socket)
    - `socket.SOCK_DGRAM` - ... (UDP socket)

  2. Propojeni lokalni ip adresy, cislo portu a soketu pomoci funkce `bind`:
  ```python
  server.bind((socket.gethostname(), 9090))
  ```
    - `socket.gethostname()` - vrati retezec s ip adresou stroje, kde bezi interpret
    - `9090` - cislo portu (u TCP obvykle `1080 <`)

  3. Musime dovolit serveru poslouchat nova pripojeni:
  ```python
  server.listen(5)
  ```
  4. `connect` metoda pro pripojeni ke vzdalenem soketu na adrese XY
  ```python
  client_socket.connect((ip, port))
  ```
  5. `accept` metoda pro prijeti pripojeni. Ziskame novy objekt, schopen prijmat
  a odesilat data a adresu spojenou se soketem na opacnem konci.

  6. `recv()` metoda urcena pro prijeti TCP zpravy
  7. `send()` metoda urcena pro odesilani TCP zpravy
</details>

---

<details>
  <summary>🌎 Server-klient, pripojeni</summary>

  #### 🔁 TCP protokol
  1. **TCP protokol** - spolehlive doruceni, garance poradi paketu, obousmerne
  2. **UDP protokol** - nespolehlive doruceni paketu, ruzne poradi, neni obousmerne

  #### 💻 Vytvoreni serveru
  1. Nahrajeme modul `socket`
  2. Vytvorime objekt pro novy socket (ipv4, tcp protokol)
  3. Navazeme socket na adresu `bind`
  4. Poslouchame na konkretnim socketu pomoci `listen`
  5. Pomoci nekonecne smycky chceme prijimat spojeni od klientu `accept`
  6. Pozdravime klienta
  ```python
  #!usr/bin/python3
  import socket


  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((socket.gethostname(), 1234))
  server_socket.listen(5)
  print("Inicializace..")

  while True:
      client_socket, client_address = server_socket.accept()
      print(f"Navazano spojeni od [{client_address}]")
      client_socket.send(bytes("Vitej na serveru", "utf-8"))
      client_socket.close()
  ```

  #### 👨 Vytvoreni klienta
  1. Nahrajeme modul `socket`
  2. Vytvorime objekt pro novy socket klienta (ipv4, tcp protokol)
  3. Pripojime se ke vzdalenem socketu `connect`
  4. Poslouchame zpravy pomoci `recv` o vhodne delce bajtu

  ```python
  #!usr/bin/python
  import socket


  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((socket.gethostname(), 1234))

  msg = client_socket.recv(1024)
  print(msg.decode("utf-8"))
  welcome_msg = client_socket.send(bytes("Pozdrav na server!", "utf-8"))
  ```
  **Pozor!**, nejprve spoustime `exam1.py` -> tedy server a potom `exam2.py`,
  tedy klienta.

</details>

---
<details>
  <summary>💼 Server-klient, pokracovani</summary>
  
  #### 💻 Upravy serveru
  1. Nahrajeme modul `select`, ten slouzi pro systemova volani Unixu. Ma 3 parametry
  - `rlist` - sockety monitorujici pro prichozi data
  - `wlist` - socket pro data k odeslani
  - `xlist` - socket monitorujici kvuli vyjimkam
  2. `select` vraci 3 listy:
  - `reading` - sockety, kde jsme obdrzeli nejaka data
  - `writing` - sockety, pripravene pro odeslani data 
  - `errors` - sockety s vyjimkami
  3. Chceme ziskat nactena data ze soketu, pokud socket odpovida soketu serveru
  ```python
  import select
  import socket


  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((socket.gethostname(), 1234))
  server_socket.listen(5)
  print("Inicializace")

  sockets_list = [server_socket]                  # list socketu pro funkci select()
  clients = {}                                    # socket-klic, header a data - hodnoty

  print(f"Posloucham spojeni na adrese: {socket.gethostname()}:1234 ...")

  while True:
      read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
      for notified_socket in read_sockets:
          if notified_socket == server_socket:
              client_socket, client_address = server_socket.accept()
              print(f"Navazano spojeni od [{client_address}]")
              client_socket.send(bytes("Vitej na serveru", "utf-8"))
  ```

  #### 👨 Upravy klienta
  1. Doplnim promennou `username` a prevedeme jej na bajty
  ```python
  my_username = input("Username:")

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((socket.gethostname(), 1234))
  client_socket.setblocking(False)

  username = my_username.encode('utf-8')
  username_header = f"{len(username):<10}".encode('utf-8')
  client_socket.send(username_header + username)

  while True:
      message = input(f'{username} > ')
      if message:
          message = message.encode('utf-8')
          message_header = f"{len(message):<10}".encode('utf-8')
          client_socket.send(message_header + message)
  ```

</details>

---

<details>
   <summary>✍  Server-klient, komunikace</summary>

  #### 💻 Strana serveru
  1. Napiseme funkci pro zpracovani prijatych zprav `receive_message`
  2. Obdrzi delku a ulozime ji do `msg_header`
  3. Pokud neobdrzim data, zavri spojeni (`return False`)
  4. Jinak pocitej delku zpravy `msg_length`
  5. Vrat slovnik se zahlavim a zpravou
  6. Pokud `rec_message` vrati `False`, klient se odhlasi
  7. Jinak posle svoje jmeno a prijme socket do `select` seznamu
  8. Soucasne pridej `username` a `header` do slovniku `clients`
  9. Pokud `notified_socket` odesila zpravu, uloz ji do `message`
  10. Pokud `meesage` neni, ukonci klienta
  11. Odstran `notified_socket` ze `sockets_list` a `clients`
  12. Pokud `message` je, ziskame uzivatele podle `notified_socket`
  13. Nakonec predame zpravu vsem, krome odesilajiciho
  ```python
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((socket.gethostname(), 1234))
  server_socket.listen(5)
  print("Inicializace")

  sockets_list = [server_socket]                  # list socketu pro funkci select()
  clients = {}                                    # socket-klic, header a data - hodnoty


  def receive_message(client_socket):
      if len(msg_header := client_socket.recv(10)):
          msg_length = int(msg_header.decode("utf-8").strip())
          return {"header": msg_header, "data": client_socket.recv(msg_length)}
      return False


  while True:
      read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
      for notified_socket in read_sockets:
          if notified_socket == server_socket:
              client_socket, client_address = server_socket.accept()
              print(f"Navazano spojeni od [{client_address}]")

              if not (user := receive_message(client_socket)):
                  continue
              sockets_list.append(client_socket)
              clients[client_socket] = user
              print(f"Nove spojeni:{client_address}, uzivatel:{user['data'].decode('utf-8')}")

          else:
              if not (message := receive_message(notified_socket)):
                  sockets_list.remove(notified_socket)
                  print(f"Spojeni ukonceni: {clients[notified_socket]['data'].decode('utf-8')}")
                  clients.pop(notified_socket)
                  continue

              user = clients[notified_socket]
              print(f"Zprava od: {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

              for client_socket in clients:
                  if client_socket != notified_socket:
                      client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
  ```

  #### 👨 Strana klienta
  1. Potrebujeme prochazet a vypisovat prijate zpravy
  2. Pokud neziskame data, server ukoncil cinnost. Zkontroluj pomoci konstanty v `header`
  3. Pokud server neskoncil, preved `header` na cislo a z nej ziskej `username`
  4. Nakonec proved to stejne pro samotnou zpravu `message_header`, `length`
  5. Pokud bude cely blok failovat, osetri s `try/except`
  ```python
  my_username = input("Username:")

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((socket.gethostname(), 1234))
  client_socket.setblocking(False)

  username_header = f"{len(my_username):<10}"
  client_socket.send(bytes(username_header + my_username, "utf-8"))

  while (message := input(f'{my_username} > ')):
      message_header = f"{len(message):<10}"
      client_socket.send(bytes(message_header + message, "utf-8"))
      try:
          while True:
              username_header = client_socket.recv(10)
              if not len(username_header):
                  print("Server ukoncen")
                  sys.exit()

              username_length = int(username_header.decode('utf-8').strip())
              username = client_socket.recv(username_length).decode('utf-8')

              message_header = client_socket.recv(10)
              message_length = int(message_header.decode('utf-8').strip())
              print(f"{username} > {client_socket.recv(message_length).decode('utf-8')}")

      except IOError:
          continue
  ```

</details>

---

