import random

igen = "ja"

while igen == "ja":
    tal = random.randint(1, 100)
    forsok = 7
    vunnit = False
    print(tal)
    print("\nVälkommen till Gissa talet!")
    print("Gissa ett tal mellan 1 och 100.")
    print("Du har 7 försök. Skriv q för att avsluta.")

    while forsok > 0 and vunnit == False:
        print("Försök kvar:", forsok)
        gissning = input("Gissa talet: ")

        if gissning.lower() == "q":
            print("Spelet avslutas!")
            raise SystemExit

        try:
            gissning = int(gissning)
        except ValueError:
            print("Skriv ett tal eller q!")
            continue

        if gissning < 1 or gissning > 100:
            print("Talet måste vara mellan 1 och 100.")
            continue

        forsok = forsok - 1

        if gissning == tal:
            print("Rätt! Du vann!")
            vunnit = True
        elif gissning < tal:
            print("För lågt!")
        else:
            print("För högt!")

    if vunnit == False:
        print("Du förlorade!")
        print("Det hemliga talet var", tal)

    igen = input("Vill du spela igen? (ja/nej): ").lower()

print("Tack för att du spelade!")
