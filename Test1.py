while True:
    vyber = input("Vyber si jaká je neznáma (Proud -> I, Napeti -> U, Odpor -> R) ") # proud-amper napeti-volt odpor-Ω

    if vyber == "proud":
        Napeti = input("Jaký je napětí?")
        Odpor = input("Jaký je Odpor?")
        Napeti =int(Napeti)
        Odpor =int(Odpor)
        if Odpor == 0:
            print("nelze dělit nulou")
        else:
            print("R=", Odpor,"Ω"," " "U=",Napeti,"V"," ","I=?")
            print("I=", Napeti,"/",Odpor)
            print("I=", Napeti/Odpor,"A")
    elif vyber == "napeti":
        Proud = input("Jaký je Proud?")
        Odpor = input("Jaký je odpor?")
        Proud = int(Proud)
        Odpor = int(Odpor)
        print("R=", Odpor,"Ω"," " "I=",Proud,"A"," ","U=?")
        print("U=", Proud,"*",Odpor)
        print("U=", Proud*Odpor,"V")
    elif vyber == "odpor":
        Napeti = input("Jaký je napětí?")
        Proud = input("Jaký je Proud?")
        Napeti =int(Napeti)
        Proud =int(Proud)
        if Proud == 0:
            print("nelze dělit nulou")
        else:
            print("U=",Napeti,"V"," ""I=", Proud,"A"," ","R=?")
            print("R=", Napeti,"/",Proud)
            print("R=", Napeti/Proud,"Ω")
    else:
        print("špatný vyběr")
        break
    opakovat=input("Chcete počítat zase?(ano, ne)")
    if opakovat == "ne":
        print("konec")
        break
