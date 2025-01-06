import os
from datetime import date
def numMexs(messaggio):
    persone={}
    for messaggi in messaggio:
        temp=messaggi.split(' ')[1]
        persona=temp.split(':')[1]
        if persona not in persone.keys():
            persone[persona]=1
        else:
            persone[persona]+=1
    
    return persone

def monthMexs(messaggio):
    mesi={}
    for messaggi in messaggio:
        temp=messaggi.split(' ')[0]
        data=temp.split(':')[-1]
        mese=data.split('-')[1]
        print(mese)
        if mese not in mesi.keys():
            mesi[mese]=1
        else:
            mesi[mese]+=1
    return mesi
    


os.system('cls')
testoFile =[]
try:
    with open('./files/messaggi.txt','r') as file:
        for lines in file:
            if lines!='\n':
                testoFile.append(lines)
except:
    print('file non trovato')

print('messaggi ricevuti:')
for messaggi in testoFile:
    print(messaggi)

x = int(input('cosa vuoi fare?\n1-Inviare un messaggio\n2-Trovare il max Da\n3-Stampare per ogni mese i messaggi\n4-Per ogni persona trovare il numero di persone con cui comunica\n'))

if x == 1 : #inviare un messaggio
    emittente=input('Chi sei? ')
    destinatario=input('A chi vuoi mandare questo messaggio? ')
    testo=input('Inserisci il contenuto del messaggio: ')
    data= date.today().strftime("%d-%m-%Y")
    output='Data:'+data+'\t'+'Da:'+emittente+'\t'+'A:'+destinatario+'\t'+'Testo:'+testo+'\n'
    x=1
    while True:
        if not(os.path.exists(f'./files/{x}.txt')):
            with open(f'./files/{x}.txt','w') as file:
               file.write(output)
            break
        else:
           x+=1
    print('Messaggio inviato!')
elif x == 2 :#Max Da
    persone=numMexs(testoFile)
    maxV=0
    maxK=''
    for key,value in persone.items():
        if value>maxV:
            maxV=value
            maxK=key
    print(f'La persona che ha mandato piu messaggi e : {maxK}')
elif x == 4 :
    print(numMexs(testoFile))
elif x == 3 :
    mesi=monthMexs(testoFile)
    print(mesi)
    for key,values in mesi.items():
        print(f'{key}:{values}')

 