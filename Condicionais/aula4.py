#####################################Condicional If#######################################
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

###################################Laço for###############################################
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
    else:
        print('Número não é primo.'. format(numero))

##################################Laço While###############################################
# nota = int(input('Informe a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Informe a nota: '))
#     print(nota)
# # a = 10
# while a < 10:
#     print(a)
#     a+=1

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
    
media = (a+b+c+d)/4
print('media: {}'.format(media))
