###########################################Conjuntos##########################################
# conjunto = {1, 2, 3, 4}
# conjunto.add(5) # adiciona
# conjunto.discard(2) #discarta

##########################################União de conjunto###################################
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjuntoUniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjuntoUniao))

##########################################Intersecção de Conjunto############################
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

#########################################Conjunto Diferença##################################
conjunto_diferenca =  conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença: {} {}'.format(conjunto_diferenca, conjunto_diferenca2))
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

####################################Pertinência#############################################
conjunto_a  = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de b: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'elefante']
conjuntoAnimais = set(lista) #set - conversão para conjunto
print(conjuntoAnimais)
listaAnimais = list(conjuntoAnimais)
print(listaAnimais)
