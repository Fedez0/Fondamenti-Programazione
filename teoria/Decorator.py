def devor(f):
    def ciao():
        x=3
        print('2')
        f()#chiama la funzione originale
        print('4')
        return 5
    print('1')
    return ciao

@devor
def stampa():
    print('3')
    return 6


print(stampa())#gli ritorna quello in ciao