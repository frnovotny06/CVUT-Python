

def middle(height, width):
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

middle(3, 9)


