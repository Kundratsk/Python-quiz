#  Quiz-Mängu Skoori Süsteem

Lihtne Python quiz-mäng, mis demonstreerib **Object-Oriented Programming (OOP)** kontseptsioone algajatele.

---

##  Programmi Oodatav Käitumine (Ülesanne)

### Mida programm teeb:

1. **Mängija loob konto**
   - Sisestab oma nime
   
2. **Vastab küsimustele**
   - 5 küsimust (multiple choice: A, B, C, D)
   - Iga küsimus on erinevast teemast (geograafia, matemaatika, loodus, ajalugu)
   
3. **Saab punkte**
   - Iga õige vastus = 20 punkti
   - Vale vastus = 0 punkti
   
4. **Näeb tulemust**
   - Lõpus näeb kogu skoori
   - Võrdlus maksimaalse skooriga
   
5. **Paremusjärjestus**
   - Näeb kõiki mängijaid sorteeritult (parim ülal)
   - Medalid kolmele parimale
   
6. **Andmete salvestamine**
   - Kõik andmed salvestatakse `scoreboard.json` faili
   - Järgmisel käivitamisel laaditakse eelmiste mängude andmed

##  OOP Kontseptsioonid, Mida Demonstreeritakse

### 1. **Klassid (Classes)**

Klassid on objektide mallid. Programm kasutab 4 klassi: Player, Question, Quiz ja ScoreBoard

### 2. **Konstruktor (__init__)**

Konstruktor on spetsiaalne meetod, mis kutsutakse välja objekti loomisel.

### 3. **Meetodid (Methods)**

Meetodid on funktsioonid klassis. Neid saab kutsuda objektil.

### 4. **Spetsiaalsed Meetodid (Magic Methods)**

Meetodid, mis algavad `__` (double underscore):

#### `__init__()` - Konstruktor
```python
def __init__(self, name):
    self.name = name
```

### 5. **Lambda funktsioonid**

Lambda on lühike funktsioon ilma `def`-ta:

```python
sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)
```

### 6. **Loendid ja Sorteerimine**

```python
self.players = []  # Tühi loend
self.players.append(player)  # Lisab mängija loendisse
```

### 7. **JSON faili töötlemine**

Programm kasutab JSON faili andmete salvestamiseks ja laadimiseks.

## Näide programmi tööst

============================================================
QUIZ GAME MENU
============================================================
1. Play game
2. View leaderboard
3. Exit
Choose (1-3): 




