import math
liczba_figur=int(input())
suma=0
for i in range(0, liczba_figur):
    dane_figury=input().split(" ")
    if len(dane_figury)==3:
        polowa_obwodu=1/2 * (float(dane_figury[0])+float(dane_figury[1])+float(dane_figury[2]))
        pole_trojkata=math.sqrt(polowa_obwodu * (polowa_obwodu-float(dane_figury[0])) * (polowa_obwodu-float(dane_figury[1])) * (polowa_obwodu-float(dane_figury[2])))
        suma+=pole_trojkata
    elif len(dane_figury)==2:
        pole_prostokata=float(dane_figury[0])*float(dane_figury[1])
        suma+=pole_prostokata
    elif len(dane_figury)==1:
        pole_kola=math.pi*float(dane_figury[0])**2
        suma+=pole_kola
    elif len(dane_figury)>3:
        print("Błąd: można podać maksymalnie 3 liczby")
        break
print(round(suma,2))
