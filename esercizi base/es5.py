import random
import os
os.system('cls')
numSegreto = random.randint(1, 100)
print('Indovina il numero segreto')
x = int(input('Inserisci il valore presunto:'))
while x!= numSegreto:
    if x > numSegreto:
        x=int(input('Valore inserito troppo alto\nInserisci il valore presunto:'))
    elif x < numSegreto:
        x=int(input('Valore inserito troppo basso\nInserisci il valore presunto:'))
    else:
        x=int(input('Valore inserito non valido\nInserisci il valore presunto:'))
print('Congratualzioni hai indovinato il numero')