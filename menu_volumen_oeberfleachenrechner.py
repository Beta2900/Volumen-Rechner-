import math                                                           #math bib weil ich Pi und Wurzel brauche

def clearscreen():                                                    # um die Konsole sauber ausehen zu lassen
    for i in range(20):
        print()

def menu():                                                                            #menü    
    clearscreen()                
    print("--------------------Menü----------------------")
    print("Bitte wählen Sie zuerst Ihren Körper aus:")
    print("(1) Kugel")
    print("(2) Quader")
    print("(3) Würfel")
    print("(4) Zylinder")
    print("(5) Kegel")
    print("(6) Pyramide")
    print("(7) Programm beenden")
    print() 
    return input("Ihre Auswahl: ")

def berechnungs_menu():                                                  #berechnungsmenü
    clearscreen()
    print("-----------Berechnung wählen-----------")
    print("(1) Oberfläche")
    print("(2) Volumen")
    print("(3) Zurück")
    print()
    return input("Ihre Auswahl: ")

#####################################KÖRPERFUNKTIONEN#################################
#Definition der funktionen.
def kugel():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        r = float(input("Radius eingeben: "))
        flaeche = 4 * math.pi * r**2
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        r = float(input("Radius eingeben: "))
        volumen = 4/3 * math.pi * r**3
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")

def quader():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        l = float(input("Länge eingeben: "))
        b = float(input("Breite eingeben: "))
        h = float(input("Höhe eingeben: "))
        flaeche = 2*(l*b + l*h + b*h)
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        l = float(input("Länge eingeben: "))
        b = float(input("Breite eingeben: "))
        h = float(input("Höhe eingeben: "))
        volumen = l*b*h
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")

def wuerfel():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        a = float(input("Kantenlänge eingeben: "))
        flaeche = 6 * a**2
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        a = float(input("Kantenlänge eingeben: "))
        volumen = a**3
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")

def zylinder():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        r = float(input("Radius eingeben: "))
        h = float(input("Höhe eingeben: "))
        flaeche = 2*math.pi*r*(r+h)
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        r = float(input("Radius eingeben: "))
        h = float(input("Höhe eingeben: "))
        volumen = math.pi*r**2*h
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")

def kegel():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        r = float(input("Radius eingeben: "))
        h = float(input("Höhe eingeben: "))
        s = math.sqrt(r**2 + h**2)  # Mantellinie # mit wurzel ( math.sqrt )
        flaeche = math.pi*r*(r + s)
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        r = float(input("Radius eingeben: "))
        h = float(input("Höhe eingeben: "))
        volumen = (1/3)*math.pi*r**2*h
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")

def pyramide():
    clearscreen()
    wahl = berechnungs_menu()
    if wahl == "1":
        l = float(input("Länge der Grundseite eingeben: "))
        b = float(input("Breite der Grundseite eingeben: "))
        h = float(input("Höhe eingeben: "))
        s_l = math.sqrt((b/2)**2 + h**2) 
        s_b = math.sqrt((l/2)**2 + h**2)
        flaeche = l*b + l*s_l + b*s_b  
        print(f"Die Oberfläche beträgt: {flaeche}")
    elif wahl == "2":
        l = float(input("Länge der Grundseite eingeben: "))
        b = float(input("Breite der Grundseite eingeben: "))
        h = float(input("Höhe eingeben: "))
        volumen = (l*b*h)/3
        print(f"Das Volumen beträgt: {volumen}")
    elif wahl == "3":
        return
    input("Enter drücken um zurückzugehen...")
        
        
#####################################HAUPTPROGRAMM#########################################


while True:
    auswahl = menu()  

    if auswahl == "7":  
        break
    elif auswahl == "1":
        kugel()  
    elif auswahl == "2":
        quader()
    elif auswahl == "3":
        wuerfel()
    elif auswahl == "4":
        zylinder()
    elif auswahl == "5":
        kegel()
    elif auswahl == "6":
        pyramide()
    else:
        print("Ungültige Auswahl!")
        input("Enter drücken, um zurückzugehen...")
            
        

