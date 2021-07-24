#########################################Listas#############################################
import statistics

lista = [1, 3, 5, 7]
listaAnimais = ['gato','elefante','cachorro']

print('O máximo valor da lista é {}\n'.format(max(lista)),
    '\nO menor valor da lista é {}\n'.format(min(lista)),
    '\nA média da lista é {}\n'.format(statistics.mean(lista)),
    '\nA Média arimética de ponto flutuante da lista é {}\n'.format(statistics.fmean(lista)),
    '\nA Mediana (valor do meio) da lista é {}\n'.format(statistics.median(lista)),
    '\nA Moda (valor mais comum) da lista é {}\n'.format(statistics.mode(lista)))

if 'lobo' in listaAnimais:
    print('\nExiste um lobo na lista.\n')
else:
    listaAnimais.append('lobo')
    print('\nAgora existe um lobo na lista\n',sorted(listaAnimais))

# soma = 0
# for x in lista:   
#     soma+=x
# print(soma)
#################################Tuplas######################################################
# lista = [1, 3, 5, 7]
# listaAnimais = ['gato','elefante','cachorro']

# listaAnimais[0] = 'macaco'
# print(listaAnimais)

# tupla = (1, 10, 12, 14)
# print(tupla[0])

# tuplaAnimal = tuple(listaAnimais)
# print(tuplaAnimal)

# listaAnimal = list(tuplaAnimal)
# print(listaAnimal)

