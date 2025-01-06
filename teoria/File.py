with open('./files/data.txt') as file:
    x = file.read() #legge tutto il file
    print(f'{x} 32132\n')


with open('./files/data.txt') as file:
    for lines in file:#lettura per riga dato che il file sono array di stringhe(immagino)
        print(lines)


with open('./files/data.txt', 'w') as file:
    for _ in range(100):
        file.write('suca\n')


try:
    with open('stocazzo.txt','w') as file:
        file.read()
except:
    print('file nono trovato')