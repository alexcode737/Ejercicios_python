num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))


while num1 > 0 :
    if num1 < 0:
        print(f'El numero {num1} no puede ser negativo')
        break
    elif num2 < 0:
        print(f'El numero {num2} no puede ser negativo')
        break
    else:
        resultado = num1 + num2
        print(f'La suma de {num1} y {num2} da como resultado')
