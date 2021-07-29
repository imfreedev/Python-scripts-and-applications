import math
import turtle
bob = turtle.Turtle()
kart = turtle.Turtle()
kart2 = turtle.Turtle()
bob.speed(0)




def cartesio (t, t2, lunghezza):
    t.rt(90)
    t.fd(lunghezza)
    t.lt(180)
    t.fd(2*lunghezza)
    t2.lt(180)
    t2.fd(lunghezza)
    t2.rt(180)
    t2.fd(2*lunghezza)
    
def polilinea(t, n, lunghezza, angolo):
    """disegna n segmenti di lunghezza e angolo variabile,
       con l0utilizzo di una tartaruga t
    """
    for i in range(n):
        t.fd(lunghezza)
        t.lt(angolo)

def arco(t, r, angolo):
    arco_lunghezza = 2* math.pi * r * angolo/360 #porzione di circonferenza
    n = int(arco_lunghezza/3)+1                  #numero di lati
    passo_lunghezza = arco_lunghezza/n           #lunghezza per ogni lato
    passo_angolo = angolo/n                      #rotazione effettuata dopo ogno lato
    print(f"angolo di {angolo} gradi")

    for i in range(int((360/angolo))):
        polilinea(t, n, passo_lunghezza, passo_angolo)
        t.lt(180-angolo)
        polilinea(t, n, passo_lunghezza, passo_angolo)
        t.lt((360-(180 + angolo))+angolo)        

print("Welcome in Flowerland created by Lorenzo Piarulli")
cartesio(kart, kart2, 300)
r = int(input("raggio dell'arco: "))
angolo = int(input("Numero di foglie: "))
angolo = 360/angolo
arco(bob,r,angolo)

input()
