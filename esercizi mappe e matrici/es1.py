import os 

os.system('cls')
x = int(input('inserisci la x: '))
y = int (input('inserisci la y: '))

matrice = [[0 for n in range(y)] for _ in range(x)]

for i in range(x):
    for j in range(y):
        matrice[i][j]= int(input(f'inserisci il valore in [{i}] [{j}]: '))

for i in range(x):
    for j in range(y):
        print(f'{matrice[i][j]} ')
    print('\n')

sum = 0
for i in range(x):
    for j in range(y):
        sum+=matrice[i][j]




sum=0
sumMax=0
indexSum=0
for i in range(x):
    sum=0
    for j in range(y):
        sum+=matrice[i][j]
    if sum > sumMax:
        sumMax=sum
        indexSum=j
print(f'riga somma piu alta:{indexSum}')

sum=0
sumMax=0
indexSum=0
for i in range(y):
    sum=0
    for j in range(x):
        sum+=matrice[j][i]
    if sum > sumMax:
        sumMax=sum
        indexSum=j
print(f'colonna somma piu alta:{indexSum}')

        
