import random
parzystych, nieparzystych = 0, 0
def parzystosc(liczba):
    if liczba % 2 == 0:
        global parzystych
        parzystych += 1
        return(liczba, "jest parzysta")
    else:
        global nieparzystych
        nieparzystych += 1
        return(liczba, "jest nieparzysta")

def losowanie():
    liczby = [random.randint(1, 20) for x in range(20)]
    print("Wylosowane liczby to:")
    for i in liczby:
        print(i, end = ' ')
    wynik = sum(liczby)
    print("\nSuma liczb wylosowanych wynosi:", wynik)
    for liczba in liczby:
        print(parzystosc(liczba))
    print("Liczba wylosowanych liczb ktore sa parzyste wynosi:", parzystych)
    print("Liczba wylosowanych liczb ktore sa nieparzyste wynosi:", nieparzystych)

def pytanie():
    loop = 0
    while 1 > loop or 5 < loop:
        try:
            loop = int(input("Ile razy ma program zadzialac?(1 - 5): "))
        except ValueError:
            print("To nie jest liczba od 1 do 5! \n")
    for x in range(loop):
        losowanie()
pytanie()
