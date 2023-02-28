from math import *


#Harjutus 5 (ininmesed)
def inimesed():
    inimesed = []
    kasvu = []
    n = int(input("Sisestage intervjueeritavate inimeste arv: "))
    
    for i in range(n):
        nimi = input("Sisestage isiku nimi: ")
        korgus = int(input("Sisestage inimese pikkus cm-des: "))
        inimesed.append(nimi)
        kasvu.append(korgus)
    
    while True:
        print("\nMENÜÜ")
        print("1. Eemaldage loendist inimene ja tema pikkus")
        print("2. Kuvage inimeste loend ja nende pikkus tähestikulises järjekorras")
        print("3. Leidke kõige pikem ja lühem inimene")
        print("4. Leidke loendist n inimese keskmine pikkus")
        print("5. Lõpeta")
        
        valik = int(input("Sisestage oma valik: "))
        
        if valik == 1:
            nimi = input("Sisestage eemaldatava isiku nimi: ")
            if nimi in inimesed:
                indeks = inimesed.index(nimi)
                inimesed.pop(indeks)
                kasvu.pop(indeks)
                print("Isik ja tema pikkus on nimekirjast eemaldatud.")
            else:
                print("Isiku loendist ei leitud.")
                
        elif valik == 2:
            sortireeritud_inimesed, sortireeritud_kasvu = zip(*sorted(zip(inimesed, kasvu)))
            print("Inimeste loend ja nende pikkus tähestikulises järjekorras:")
            for i in range(len(sortireeritud_inimesed)):
                print(sortireeritud_inimesed[i], sortireeritud_kasvu[i], "cm")
                
        elif valik == 3:
            korgeim = max(kasvu)
            luhim = min(kasvu)
            indeks_korgeim = kasvu.index(korgeim)
            indeks_luhim = kasvu.index(luhim)
            print("Korgeim inimine:", inimesed[indeks_korgeim], korgeim, "cm")
            print("Luhim inimene:", inimesed[indeks_luhim], luhim, "cm")
            
        elif valik == 4:
            n = int(input("Sisestage inimeste arv keskmise pikkuse leidmiseks: "))
            nimed = []
            for i in range(n):
                nimi = input("Sisestage isiku nimi: ")
                if nimi in inimesed:
                    nimed.append(nimi)
                else:
                    print("Isiku loendist ei leitud.")
            
            if nimed:
                suuruseid = [kasvu[inimesed.index(name)] for name in nimed]
                keskminesuurus = sum(suuruseid) / len(suuruseid)
                print("Valitud inimeste keskmine pikkus:", keskminesuurus, "cm")
                
        elif valik == 5:
            break
            
        else:
            print("Vale. Proovi uuesti. ")