vet = [3,3,1,3,4,2,3,42,5]

tempV = vet[::-1] # come copiare tutto con reverse

tempV =set(tempV)
print(tempV)
if(len(vet)==len(tempV)):
    print('non ci sono duplicati')
else:
    print('ci stanno')