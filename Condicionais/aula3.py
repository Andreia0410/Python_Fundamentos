# Condicionais IF, ELIF E ELESE

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))

# if a>b and a>c:
#     print('O maior número é {}'.format(a))
# elif b>a and b>c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa!')

#################################################################################

# a = int(input('Digite um valor: '))
# b = int(input('Digite um valor: '))

# resto_a = a % 2
# resto_b = b % 2
# # resto = a % 2

# if resto_a == 0 or not resto_b > 0:
#     print('Número é par')
# else:
#     print('Número é ímpar')

####################################################################################

a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
    
media = (a+b+c+d)/4
print('media: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errado.')
