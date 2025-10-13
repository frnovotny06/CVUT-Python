


def clock(widht):
    if not widht % 2 or widht < 3 or widht > 20:
        return 1
    i = 1
    k = widht
    m = widht
    j = widht - 2
    print(" $"+ j * "-"+ "$")
    m -= 2
    while m >= 1:

        print(" " * i , m * "x")

        m -= 2
        i += 1
    i -=1
    while abs(m) < k - 2:
        m -= 2
        i -= 1
        print(" " * i , abs(m) * "x")
    print(" $" + j * "-" + "$")


clock(7)

def middle(height, width):
    if width < 3 or width> 20:
        return 1
    elif width % 2 == 0:
        return 1
    if height > width:
        return 2
    i = 3
    k = width % 2 * 2
    l = int(width / 2)
    u = int(width / 2)
    o = 0
    print( l * " " , "o")

    while i  <= width + 2:

        print( l * " " +i * "@")
        i +=2
        k -= 1
        l -= 1
    p = 1
    while p <= height:
        print("@"+ width * "x"+ "@" )
        p += 1
    while width >= 1:
        print( o* " "+  (width + 2) * "@")
        o += 1
        width -= 2

    print( u * " ", "o")

middle(3, 5)


def house(width, height,  character):

    if width < 3 or width> 20:
        return 1
    elif width % 2 == 0:
        return 1
    if height > width:
        return 2
    if len(character) == 1 and not character.isalpha() and not character.islower():
        return 3

    i = 3
    k = width % 2 * 2
    l = int(width / 2)
    u = int(width / 2)
    o = 0
    print(l * " ", "^")

    while i <= width :
        print(l * " " + i * "^")
        i += 2
        k -= 1
        l -= 1

    while o < height:
        print(" |" + (width - 2) * character + "|")
        o += 1
house(9, 5, "o")