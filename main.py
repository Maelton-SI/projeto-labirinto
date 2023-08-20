from Pilha import Pilha
from Labirinto import Labirinto
from Funcoes import eh_possivel_sair

def main():   
    meu_labirinto = Labirinto(11,8)
    
    meu_labirinto.imprime_matriz_labirinto()
    print("Eh possivel sair: ", eh_possivel_sair(meu_labirinto))

if __name__ == '__main__':
    main()
