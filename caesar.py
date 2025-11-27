alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def dekoduj(zasifrovany, odposlechnuty):

    if len(odposlechnuty) == len(zasifrovany) and odposlechnuty.isalpha() == False or zasifrovany.isalpha == False :
        print("Error: Chybny vstup!")
        return None
    if len(odposlechnuty) != len(zasifrovany):
        print("Error: Chybna delka vstupu!")
        return None


    if odposlechnuty.isalpha() != True:
        print("Error: Chybny vstup!")
        return None
    if zasifrovany.isalpha() != True:
        print("Error: Chybny vstup!")
        return None


    nejtxt = ""
    nejlepsitext = 0
    for i in range(len(alphabet)):
        txt= ""

        x = alphabet.index(zasifrovany[0])
        y = alphabet.index(odposlechnuty[0])
        lenght = y - x
        shodacount = 0
        for pismeno in zasifrovany:
            index = alphabet.index(pismeno)
            txt += alphabet[(index - i) % len(alphabet)]
        for a,b in zip(txt , odposlechnuty):
            o = 0
            if a == b:
                shodacount += 1
            if b not in alphabet:

                txt.replace(a, "x")




        if shodacount >= nejlepsitext:
            nejlepsitext = shodacount
            nejtxt = txt




    return nejtxt



dekoduj("xUbbemehbT", "XYlloworld")
dekoduj("mnoXYhnTLJ", "JCudvgtXRi")
dekoduj("fghQRa-CEC", "scbdeMKARZ")
dekoduj("fghQRa", "scbdeMK")