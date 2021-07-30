a =int(input('Digite um valor: '))
b = int(input('Digite um valor: '))

soma = a + b
sub  = a - b
multiplicacao = a * b
divisao = a/b
resto = a%b

print(type(soma))
print(sub)
print(multiplicacao)
print(int(divisao))
print(type(divisao))
#print('soma:'+str(soma))
print('soma: {soma}. \nSubtracao: {sub}.' 
      '\nmultiplicacao: {multiplicacao}. \ndivisao: {divisao}'
      .format(soma=soma, sub=sub, multiplicacao=multiplicacao, divisao=divisao))
