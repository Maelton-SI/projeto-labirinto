from Pilha import Pilha

class Desbravador:
    def __init__(self):
    #def __init__(self, labirinto):
        #self.mapa = labirinto.mapa
        self.mapa = [

['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

        self.coordenada = (1,0)
        self.direcao = "direita"
        self.memoria_trajeto = Pilha()
        self.memoria_trajeto_sem_saida = list()
        
        self.deu_primeiro_passo = False

    def set_direcao_direita(self):
        self.direcao = "direita"
    
    def set_direcao_baixo(self):
        self.direcao = "baixo"
    
    def volta_passo(self):
        self.memoria_trajeto_sem_saida.append(self.coordenada)
        self.coordenada = self.memoria_trajeto.pop()
        
        print("oi",self.coordenada)

    def dar_passo(self):
        coordenada_atual = self.coordenada
    
        if self.direcao == "direita":
            if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                    self.memoria_trajeto.push(self.coordenada)
                    self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                    self.deu_primeiro_passo = True
                    print(self.coordenada)
                else:
                    if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                        if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                            self.set_direcao_baixo()
                            self.memoria_trajeto.push(self.coordenada)
                            self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                            self.deu_primeiro_passo = True
                            print(self.coordenada)
            else:
                if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                    if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                        self.set_direcao_baixo()
                        self.memoria_trajeto.push(self.coordenada)
                        self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                        self.deu_primeiro_passo = True
                        print(self.coordenada)

        elif self.direcao == "baixo":
            if self.mapa[ self.coordenada[0]+1 ][ self.coordenada[-1] ] != "#":
                if (self.coordenada[0]+1, self.coordenada[-1]) not in self.memoria_trajeto_sem_saida:
                    self.memoria_trajeto.push(self.coordenada)
                    self.coordenada = (self.coordenada[0]+1, self.coordenada[-1])
                    self.deu_primeiro_passo = True
                    print(self.coordenada)
                else:
                    if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                        if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                            self.set_direcao_direita()
                            self.memoria_trajeto.push(self.coordenada)
                            self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                            self.deu_primeiro_passo = True
                            print(self.coordenada)
            else:
                if self.mapa[ self.coordenada[0] ][ self.coordenada[-1]+1 ] != "#":
                    if (self.coordenada[0], self.coordenada[-1]+1) not in self.memoria_trajeto_sem_saida:
                        self.set_direcao_direita()
                        self.memoria_trajeto.push(self.coordenada)
                        self.coordenada = (self.coordenada[0], self.coordenada[-1]+1)
                        self.deu_primeiro_passo = True
                        print(self.coordenada)
        
        if coordenada_atual == self.coordenada:
            
            if self.deu_primeiro_passo == False:
                self.deu_primeiro_passo = True
            else:
                self.volta_passo()