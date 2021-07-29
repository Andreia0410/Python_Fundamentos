# diretorio = 'D:/DIO/Python_Fundamentos/'
import statistics
import shutil


def escreve_arquivo(texto):
    arquivo = open('notas.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('notas.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for nota in aluno_nota:
        lista_notas = nota.split(',')
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0)
        print(lista_notas)
        #media = lambda notas: statistics.mean([int(i) for i in notas])
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(statistics.mean(aluno))

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/DIO/Python_Fundamentos/aluno_notas.txt')     
        
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/DIO/aluno_notas.txt')
    

if __name__=='__main__':
    move_arquivo('aluno_notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # print(media_notas('notas.txt'))
    # escreve_arquivo('Primeira linha.\n')
    # aluno = 'Rafael, 7, 8, 8, 9\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('notas.txt')
