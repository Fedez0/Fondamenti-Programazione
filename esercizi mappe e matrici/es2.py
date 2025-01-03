import os 

os.system('cls')



votiStundente={}
listaStudenti=[]

while True:
    x=int(input('1. Inserisci Studente\n2. Aggiungi voto a Studente\n3. Stampa\n4. Calcola media voti Studente\n5. Esci\n'))
    if x == 1:
        listaStudenti.append(input('inserisci nome: '))
    elif x == 2:
        nome=input('inserisci il nome a cui vuoi inserire un voto: ')
        if nome in listaStudenti:
            if nome in votiStundente.keys():
                votiStundente[nome].append(int(input('inserisci il voto: ')))
            else: 
                votiStundente[nome]=[int(input('inserisci il voto: '))]
        else: 
            print('nome non trovato')
    elif x == 3:
        for key,values in votiStundente.items():
            print(f'{key} : {values},')
        print(votiStundente)
    elif x == 4:
        for key,values in votiStundente.items():
            print(f'{key} : {sum(values)/len(values)},')
    elif x == 5:
        break
    print('\n\n')