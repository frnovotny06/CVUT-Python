from operator import index

matice = [[1, 2, 3, 4]
        , [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14 , 15, 16]]

def spirala (matice):
    newmatrix = []

    while matice:
        if matice:
            newmatrix += matice.pop(0)
        if matice and matice[0]:
            for radek in matice:

                newmatrix.append( radek.pop())
        if matice:
            newmatrix +=matice.pop()[::-1]

        if matice:
            for randek in matice[::-1]:
                newmatrix.append(randek.pop(0))






    print(newmatrix)




abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
klicabeceda = "abcdefghijklmnopqrstuvwxyz"

def sifra(zprava, klic):


    if klic.isalpha or klic.islower():
        note = True

    else:
        note = False



    while len(zprava) > len(klic):
        klic += klic * 2

    print(zprava, klic)

    i = 0
    zasifrovanazprava = ""
    for pismeno in range(len(zprava)):


        x = klicabeceda.find(klic[i])

        y = abeceda.find(zprava[i])



        zasifrovanazprava += abeceda[(x+y) % len(abeceda)]

        i = i + 1
    if note == False:
        zasifrovanazprava = "None"

    print((note ,zasifrovanazprava))



def ctverec(velikost, souradnice, znak):

    if len(znak) != 1:
        return "Error"




    if velikost < 3 or velikost > 10:
        return "Error"

    if souradnice < 1 or souradnice > 10 :
        return "Error"


    if souradnice == velikost:
        print(znak * (velikost + souradnice - 1))
        for i in range(velikost - 2):
            print(znak + " " * (velikost - 2) + znak + " " * (velikost - 2) + znak)
        print(znak * (velikost + souradnice - 1))

    if souradnice < velikost:

        print(znak * (velikost + souradnice-1))

        for i in range(velikost - 2):
            print(znak + " " * (souradnice-2) + znak + " " * (velikost - souradnice -1) + znak + " " * (souradnice-2)+ znak)
        print(znak * (velikost + souradnice-1))





    if souradnice > velikost:
        print(znak * (velikost + souradnice))
        for i in range(velikost -2):
            print(znak + " " * (velikost - 2) + znak + " " * (souradnice - velikost) + znak + " " * (velikost - 2) + znak)
        print(znak * velikost + " " * (souradnice - velikost) + znak * velikost)


ctverec(5,2,'cc')

