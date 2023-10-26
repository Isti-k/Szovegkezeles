def szepnapvan():
    szoveg: str = "Szép nap van!"

    '''Írd ki a szöveget első karakterét!'''

    print("1. ", szoveg[0])
    '''Írd ki a szöveg 2. karakterét!'''
    print("2. ", szoveg[1])
    '''Írd ki a szöveg hosszát!'''
    print("A hossz: ", len(szoveg))
    '''Írd ki a szöveg utolsó karakterét!'''
    print("utolsó ", szoveg[len(szoveg)-1])

    '''Írd ki a szöveg karaktereit egymás alá betűnként!'''
    i:int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i += 1

def szövegkezelés():
    szoveg:str = "Ez egy teszt szöveg."
    print(szoveg)
    print(szoveg.upper())
    print(szoveg)

    '''Van-e a szövegben 'teszt' szöveg'''
    x:int = szoveg.find("teszt")
    if x>0:
        print("van benne teszt szöveg")
    else:
        print("nincs bene teszt szöveg")
    '''A SZOVEG választóban hol szerepel először a 's' betű?'''
    print(szoveg.index("s"), ". helyen szerpel az s betű")
    '''Alskítsd át minden szó kedőbetűjét nagybetűssé!'''
    print(szoveg.title())
    '''Cseréd ki a teszt szót próbára'''
    print(szoveg.replace("teszt", "próba"))

def aszoveg_visszafele(szoveg:str):
    '''A paraméterben kapott szöveg viszafelé kiírva egymás mellé a betű'''
    #print(szoveg[::-1])
    i: int = len(szoveg)
    while i !=0: #i>=0
        print(szoveg[i-1], end=" ")
        i -= 1

def a_betuk_szama(szoveg:str):
    '''Hány "a" betű van a szövegben?'''
    #print(szoveg.count("a"))
    i:int = 0
    a_szam:int = 0
    while i<len(szoveg):
        if szoveg[i] == 'a':
            a_szam += 1
        i += 1
    print("A betűk száma: ",a_szam)