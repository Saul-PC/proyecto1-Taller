def sepDig(n): 
        d1 = n % 10
        n //= 10
        d2 = n % 10
        n //= 10
        d3 = n % 10
        n //= 10
        d4 = n % 10
        n //= 10
        d5 = n
        return [d5,d4,d3,d2,d1]
"""
Dominio: un número entero de 4 o 5 dígitos
Codominio: Una lista de 5 números enteros

"""
def digRep(l,r):
    for i in l:
        if l.count(i) > r:
            return False
    return True
"""
Dominio: una lista de 10 números enteros y un entero r
Codominio: Verdadero si en la lista de 10 enteros se repiten
cada uno de sus dígitos r veces o menos, falso si esto no se cumple

"""

t = int(input())
while t:

    t -= 1
    c, r = map(int, input().split())
    
    for den in range(10000//c,100000//c):

        num = den * c
        listaDen = sepDig(den)
        listaNum = sepDig(num)

        if len(listaDen) >= 4:
        
            if digRep(listaDen + listaNum, r):
                print(str(num) + "/" + str(den) + "=" + str(c))
