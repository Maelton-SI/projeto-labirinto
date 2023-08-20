from random import randint
from Pilha import Pilha

class Labirinto:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas

        self.inicio = (1,0)
        self.fim = (linhas-2,colunas-1)
        
        self.livre = ' '
        self.ocupado = '#'
        self.parede  = '#'
        
        self.mapa = self.gera_labirinto()
        
        self.coordenada = (1,0)
        self.direcao = "direita"
        self.memoria_trajeto = Pilha()
        self.memoria_trajeto_sem_saida = list()
        
        self.deu_primeiro_passo = False
    
    def __str__(self):
        mapa = ""
        for i in self.mapa:
            mapa += "".join(i)
            mapa += "\n"
        return mapa
    
    def gera_labirinto(self):
        lab = [([self.parede]*self.colunas)]
        for i in range(1,self.linhas-1):
            linha = [self.livre] * self.colunas
            for j in range(self.colunas):
                if randint(0,7) in [0,1]:
                    linha[j] = self.ocupado
                if j in [0,self.colunas-1]:
                    linha[j] = self.parede
            lab.append(linha)
        lab.append([self.parede]*self.colunas)
        lab[self.inicio[0]][self.inicio[1]] = self.livre
        lab[self.fim[0]][self.fim[1]] = self.livre
        return lab
    
    def imprime_matriz_labirinto(self):
        for linha in self.mapa:
            print(linha)
        print("\n")

    def set_direcao_direita(self):
        self.direcao = "direita"
    
    def set_direcao_baixo(self):
        self.direcao = "baixo"
    
    def volta_passo(self):
        self.memoria_trajeto_sem_saida.append(self.coordenada)
        self.coordenada = self.memoria_trajeto.pop()
        
        #print("voltei",self.coordenada)

    def dar_passo(self):
        coordenada_atual = self.coordenada
    
        if self.direcao == "direita":
            if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                    self.memoria_trajeto.push(self.coordenada)
                    self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                    self.deu_primeiro_passo = True
                    #print("avancei", self.coordenada)
                else:
                    if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                        if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                            self.set_direcao_baixo()
                            self.memoria_trajeto.push(self.coordenada)
                            self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                            self.deu_primeiro_passo = True
                            #print("avancei", self.coordenada)
            else:
                if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                    if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                        self.set_direcao_baixo()
                        self.memoria_trajeto.push(self.coordenada)
                        self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                        self.deu_primeiro_passo = True
                        #print("avancei", self.coordenada)

        elif self.direcao == "baixo":
            if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                    self.memoria_trajeto.push(self.coordenada)
                    self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                    self.deu_primeiro_passo = True
                    #print("avancei", self.coordenada)
                else:
                    if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                        if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                            self.set_direcao_direita()
                            self.memoria_trajeto.push(self.coordenada)
                            self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                            self.deu_primeiro_passo = True
                            #print("avancei", self.coordenada)
            else:
                if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                    if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                        self.set_direcao_direita()
                        self.memoria_trajeto.push(self.coordenada)
                        self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                        self.deu_primeiro_passo = True
                        #print("avancei", self.coordenada)
        
        if coordenada_atual == self.coordenada:
            
            if self.deu_primeiro_passo == False:
                self.deu_primeiro_passo = True
            else:
                self.volta_passo()

if __name__ == '__main__':
    print()