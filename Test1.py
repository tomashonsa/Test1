while True:
    vyber = input("Vyber si jaká je neznáma (Proud -> I, Napeti -> U, Odpor -> R) ") # proud-amper napeti-volt odpor-Ω

    if vyber == "I":
        Napeti = input("Jaký je napětí?")
        Odpor = input("Jaký je Odpor?")
        Napeti =float(Napeti)
        Odpor =float(Odpor)
        if Odpor <= 0:
            print("nelze dělit nulou nebo zápornou hodnotou")
        else:
            print("R=", Odpor,"Ω"," " "U=",Napeti,"V"," ","I=?")
            print("I=", Napeti,"/",Odpor)
            print("I=", Napeti/Odpor,"A")
    elif vyber == "U":
        Proud = input("Jaký je Proud?")
        Odpor = input("Jaký je odpor?")
        Proud = float(Proud)
        Odpor = float(Odpor)
        print("R=", Odpor,"Ω"," " "I=",Proud,"A"," ","U=?")
        print("U=", Proud,"*",Odpor)
        print("U=", Proud*Odpor,"V")
    elif vyber == "R":
        Napeti = input("Jaký je napětí?")
        Proud = input("Jaký je Proud?")
        Napeti =float(Napeti)
        Proud =float(Proud)
        if Proud <= 0:
            print("nelze dělit nulou nebo zápornou hodnotou")
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