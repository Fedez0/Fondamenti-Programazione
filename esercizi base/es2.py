num1 = int(input('inserisci il primo numero: '))
op = input('l\'operando: ')
num2 = int(input('inserisci il secondo numero: '))
ris = 0
if op == '+':
    ris = num1 + num2
elif op == '-':
    ris = num1 - num2
elif op == '*':
    ris = num1 * num2
elif op == '/':
    ris = num1 / num2
else:
    print('openrando inserito non valido')
    exit()

print(f'La tua operazione riuslta {ris}')