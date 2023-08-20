def eh_possivel_sair(labirinto):
    while True:
        if labirinto.coordenada == labirinto.fim:
            return True
        elif labirinto.coordenada == labirinto.inicio and labirinto.deu_primeiro_passo == True:
            return False
        
        labirinto.dar_passo()

if __name__ == "__main__":
    print()
