
def mergesort(a):
    n = len(a)

    if n <= 1:
        return a

    mitad = n // 2
    arrayUno = a[:mitad]
    arrayDos = a[mitad:]

    arrayUno = mergesort(arrayUno)
    arrayDos = mergesort(arrayDos)

    return merge(arrayUno, arrayDos)


def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)

    while len(a) > 0:
        c.append(a[0])
        a.pop(0)

    while len(b) > 0:
        c.append(b[0])
        b.pop(0)

    return c


numeros = []

for i in range(6):
    numero = int(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

print("Original:", numeros)
print("Ordenado:", mergesort(numeros))
