def pitagoras(x, y):
    f = max(abs(x), abs(y))
    a = min(abs(x), abs(y))
    for num in range(3):
        b = (a/f)**2
        c = b/(4+b)
        f = f+2*c*f 
        a = c*a
    return f


def norma(lista):
    k = 0
    for num in lista:
        k = pitagoras(num, k)

    return k


print(norma([3, 4, 12]))