from random import randint

class Labirinto:
    def __init__(self, linhas, colunas):
        self.inicio = (1,0)
        self.fim = (linhas-2,colunas-1)
        self.livre = ' '
        self.ocupado = '#'
        self.parede  = '#'
        self.mapa = self.gera_labirinto(linhas, colunas)

    def __str__(self):
        mapa = ""
        for i in self.mapa:
            mapa += "".join(i)
            mapa += "\n"
        return mapa
    
    def gera_labirinto(self,m,n):
        lab = [([self.parede]*n)]
        for i in range(1,m-1):
            linha = [self.livre] * n
            for j in range(n):
                if randint(0,7) in [0,1]:
                    linha[j] = self.ocupado
                if j in [0,n-1]:
                    linha[j] = self.parede
            lab.append(linha)
        lab.append([self.parede]*n)
        lab[self.inicio[0]][self.inicio[1]] = self.livre
        lab[self.fim[0]][self.fim[1]] = self.livre
        return lab

if __name__ == '__main__':
    print()