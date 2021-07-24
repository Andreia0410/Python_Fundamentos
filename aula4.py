# numero = int(input('Informe um número: '))

# div = 0
# for x in range(1, numero+1):
#     resto = numero%x
#     print(x, resto)
#     if resto == 0:
#         div =+ 1
        
# if div == 2:
#     print('Número {} é primo'.format(numero))
# else:
#     print('Número não é primo.'. format(numero))

a = int(input('Informe um valor: '))
for numero in range(a+1):
    div = 0
    for x in range(1, numero+1):
        resto = numero%x
        # print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(numero)
    # else:
    #     print('Número não é primo.'. format(numero))
    