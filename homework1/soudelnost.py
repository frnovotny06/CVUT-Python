import math

def tabulka (k):
    if not isinstance(k ,int) or k not in range (1,100):
        print("ERROR")
        return


    n = 1

    while n != k +1:
            m = 1
            while m <= k:
                if m == k:
                    if math.gcd(n, m) > 1:
                        print("x", end="")
                        break
                    else:
                        print(" ", end="")
                        break
                if math.gcd(n, m) > 1:
                    print("x" , end="|")
                else:
                    print(" ", end="|")
                m += 1
            print()
            n += 1
            if n != k +1:
                print(((k*2) - 1) * "-")
            else:
                break

tabulka(7)
