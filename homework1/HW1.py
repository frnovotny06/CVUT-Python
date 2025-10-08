


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


clock(11)




