class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        i = 0
        j = 0

        # Dicionário para mapear comandos para funções de movimento
        comandos = {
            "RIGHT": lambda i, j: (i, j + 1),
            "LEFT": lambda i, j: (i, j - 1),
            "DOWN": lambda i, j: (i + 1, j),
            "UP": lambda i, j: (i - 1, j)
        }

        for command in commands:
            # Obter a função correspondente e atualizar (i, j)
            if command in comandos:
                i, j = comandos[command](i, j)
            else:
                return "Error"

        matriz = criar_matriz_nxn(n)
        return matriz[i][j]

def criar_matriz_nxn(n):
    # Inicializar a matriz
    matriz = [[0] * n for _ in range(n)]
    
    # Preencher a matriz com valores de 0 a n*n - 1
    valor = 0
    for i in range(n):
        for j in range(n):
            matriz[i][j] = valor
            valor += 1

    return matriz