import time
t0 = time.time()
def sepDig(n):
    if n < 10000:
        d1 = n % 10
        n //= 10
        d2 = n % 10
        n //= 10
        d3 = n % 10
        n //= 10
        d4 = n 
        return [d4,d3,d2,d1]
    if n >= 10000: 
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
    
    


def digRep(l,cantreps):
    for i in l:
        if l.count(i) > cantreps:
            return False
    return True



t = int(input())

while t:

    t -= 1
    c, r = map(int, input().split())

    
    for den in range(10000//c,100000//c):

        num = den * c
        listaDen = sepDig(den)
        listaNum = sepDig(num)

        if len(listaDen) >= 4:

            cerosLista = 5 - len(listaDen)

            for i in range(cerosLista):
                listaDen.insert(0,0)
        
            if digRep(listaDen + listaNum, r):
                print(str(num) + "/" + str(den) + "=" + str(c))
