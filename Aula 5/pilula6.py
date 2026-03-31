def numeroPrimo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

valor = int(input('N = '))
if numeroPrimo(valor):
    print('É primo')
else:
    print('Não é primo')