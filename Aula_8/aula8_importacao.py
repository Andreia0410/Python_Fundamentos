from typing import Mapping
from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_palavras import contador_letras, teste


if __name__=='__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'girafa']
    print(contador_letras(lista))
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista: {}'.format(total_letras))
    print(teste())
    