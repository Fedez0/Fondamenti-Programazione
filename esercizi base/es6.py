import os
os.system('cls')

numPrimi= [1]

for n in range(2,100+1):
    temp = 0
    for i in numPrimi:
        if n%i == 0:
            temp+=1
    if temp == 1:
        numPrimi.append(n)
print(numPrimi)