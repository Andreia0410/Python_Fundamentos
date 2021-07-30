# Função é tudo que retorna um valor
# Método é o que não retorna.

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
            
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
            
    def aumenta_canal(self):
        if self.canal:
            self.canal +=1
        else:
            return self.canal
        
    def diminui_canal(self):
        if self.canal:
            self.canal -=1
        else:
            return self.canal
        

print(__name__)
if __name__ == '__main__':     
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()  
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
