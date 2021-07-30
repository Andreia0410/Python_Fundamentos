#####################################Funções anônimas lambdas"######################################
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'girafa']
contador_letras(lista_animais)

soma = lambda a, b: a + b
sub = lambda a, b: a-b

print(sub(7, 3))
print(soma(5, 10))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
subtracao = calculadora['subtracao']
divisao = calculadora['divisao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 6)))
