sum = 0 
for n in range(100+1):
    if n % 2 == 0:
        print(n)
        sum+=n

print(f'La tua somma e\' {sum}')