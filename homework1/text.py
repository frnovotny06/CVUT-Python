import math


def histogram(text, scale, case_sensitive=False):

    if case_sensitive == False:
        text = text.lower()

    dictionary = {}

    for i in text:
         if i.isalpha():
            if i not in dictionary:
                dictionary[i] = 0
            dictionary[i]+= 1
    for i in dictionary:
        pass
    serazene = sorted(dictionary.items())

    highest = 0
    for k,v in serazene:
        if v > highest:
            highest = v



    l = highest

    newscale = (scale / l)
    for k, v in serazene:


        if scale != 0 :


                print(f"{k}: {('*' * math.floor(v* newscale))}")

        else:

                print(f"{k}: {'*' * v}")

    return serazene


def serad (text, metoda, case_sensitive=False):


    if case_sensitive == True:
        pass



    newtext= []
    for i in text.split():
        i = i.strip(".,!?")
        if len(i) >= 3:
            newtext.append(i)


    if metoda == 0:

        return sorted(newtext , key=lambda s:(-len(s),s))



    if metoda == 1:
        samohlasky = "aeiou"


        newtext.sort( key= lambda slovo: (-sum(1 for pismeno in slovo.lower() if pismeno not in samohlasky), slovo))
        return newtext



    newdict = {}
    if metoda == 2:
        newtext.sort(key=lambda s :(nejpismeno(s),s))
        return newtext


    if metoda == 3:
        return sorted(newtext, key=lambda slovo: (len(slovo), slovo))

def nejpismeno(text):

    dictionary = {}

    for i in text:
        if i.isalpha():
            if i not in dictionary:
                dictionary[i] = 0
            dictionary[i] += 1
    for i in dictionary:
        pass
    serazene = sorted(dictionary.items())

    highest = 0
    for k, v in serazene:
        if v > highest:
            highest = v

    return highest * -1




histogram("Aaaach, to je kraaasa", 4 )
print(serad('auxiliary endeavors towards recent have been very You', 0, True))