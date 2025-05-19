import pygame
import random 

#Inicializacoes
pygame.init()

#constante da tela
LARGUARA = 300
ALTURA = 600
TAMANHO_BLOCO = 30
COLUNAS = LARGUARA // TAMANHO_BLOCO
LINHAS = ALTURA // TAMANHO_BLOCO

#cores
PRETO = (0,0,0)
CINZA =(128,128,128)
CORES =[
    (0,255,255), # I
    (0,0,255),   # J
    (255,165,0), # L
    (0,255,0),   # O
    (128,0,128), # S
    (255,0,0)    # T
]

#Formantos das peças (Tetriminos)
PEÇAS = [
    [[1, 1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]]

]
# Classe da peça
class peca:
    def __init__(self, x, y, forma ):
        self .x = x
        self .y = y
        self .forma = forma
        self .cor = random.choice(CORES)
        self .rotacao = 0
        pass
    def imagem(self):
        return self.forma[self.rotacao % len(self.forma)]
    
    def rotacionar(self):
        self.rotacao = (self.rotacao + 1) % len(self.forma)

# Criação da grade
def criar_grade(travado={}): 
    grid = [[PRETO for _  in  range(COLUNAS)] for _ in range(LINHAS)]
    for y in range(LINHAS):
        for x in range(COLUNAS):
            if (x, y) in travado:
                grid[y][x] = travado[(x, y)]

    return 
            
# Converter formato da peça para posições na grade
def converter_forma(peca):    
    posicoes = []
    forma = peca.imagem()
    
    for i, linha in enumerate(forma):
        for j, bloco in enumerate(linha):
            if bloco: 
                posicoes.append((peca.x + j, peca.y + i)) 
    return posicoes

#Verifica posição é valida 
def posicao_valida(peca, grid):
    posicoes = converter_forma(peca)
    for x, y in posicoes:
        if x < 0 or x >= COLUNAS or y >= LINHAS:
            return False 
        if y >= 0 and grid[y][x] != PRETO:
            return False
    return True
    
#Remover linhas completas
 def limpar_linhas(grid, travado):
    linhas_removidas = 0 
    for i in range(len(grid,-1, -1, -1):
        if PRETO not in grid[i]:
        linhas_removidas += 1
        idx = i 
        for j in range (COLUNAS):
        try:
            del travado[(j, i)]
            except:
                continue
    if linhas_removidas > 0:
        for chave in  sorted(travado, key=lambda k: k[1]) [::-1]:
        x, y = chave 
        if y < idx:
            nova_chave = (x, y + linhas_removidas)
            travado[nova_chave]  = travado.pop(chave)
            return linhas_removidas 
    
#Desenhar grade 
 def desenhar_grid(tela,grid):
        
    
    forma = converter_forma(peca_ataual)
    for x, y in  forma:
        if y >= 0:
            grid[y][x] = peca_atual.cor

    if troca_peca:
        for pos in forma:
            if y >= 0:
                grid[y][x] = peca_atual.cor

        if troca_peca:
            for pos in forma:
                x, y = pos    
                if y < 0:
                    rodando = False
                    break
                travando[(x, y)] peca_atual.cor
            peca_atual = proxima_peca
            proxima_peca = peca(3, 0, random.choice(PEÇAS))
            troca_peca = False
            pontuacao += limpar_linhas(grid, travado) * 10

        tela.fill(PRETO)
        desenhar_grid(tela, grid)
        pygame.display.update()

    game_over_text(tela)
    pygame.display.update()
    pygame.tim.wait(2000)
    pygame.quit()

 if __name__ == "__main__":
     main()           