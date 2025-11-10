alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"






def dekoduj(zasifrovany , odposlechnuty):

    if len(zasifrovany) != len(odposlechnuty):
        print("Spatny vstup")

    nejviceshod = -1
    nejshoda = ""


    for shift in range(len(alphabet)):
        txt = ""


        for ch in zasifrovany:
            if ch in alphabet:
                idx = alphabet.index(ch)
                txt += alphabet[(idx - shift) % len(alphabet)]
            else:
                txt += ch
        shoda = 0
        for a, b in zip(txt, odposlechnuty):
            if b != '?' and a == b:
                shoda += 1
        if shoda > nejviceshod:
            nejviceshod = shoda
            nejshoda = txt

    print(nejshoda)
    return nejshoda


dekoduj("xUbbemehbT", "??lloworld")