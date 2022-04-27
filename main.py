import math
liczba_figur=int(input())
for i in range(liczba_figur):
    dane_figury=input().split(" ")
    suma=0
    if len(dane_figury)==3:
        polowa_obwodu=1/2*(float(dane_figury[0])|+float(dane_figury[1])+float(dane_figury[2]))
        pole_trojkata=math.sqrt(polowa_obwodu * (polowa_obwodu-dane_figury[0]) * (polowa_obwodu-dane_figury[1]) * (polowa_obwodu-dane_figury[2]))
        suma+=pole_trojkata
    elif len(dane_figury)==2:
        pole_prostokata=float(dane_figury[0])*float(dane_figury[1])
        suma+=pole_prostokata
    elif len(dane_figury)==1:
        pole_kola=math.pi*float(dane_figury[0])**2
        suma+=pole_kola
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
    print(round(suma,2))
