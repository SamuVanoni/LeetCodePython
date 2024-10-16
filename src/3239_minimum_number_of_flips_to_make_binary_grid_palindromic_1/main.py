class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid); c = len(grid[0])
        rf = 0; cf = 0

        for i in range(r): # Loop nos elementos da lista
            for j in range(c//2): # Loop na metade dos elementos de dentro de cada lista
                if grid[i][j] != grid[i][c-j-1]:
                    rf += 1
        
        for i in range(c): # Loop em cada elemento dentro da lista
            for j in range(r//2): # Loop na metade dos elementos da lista
                if grid[j][i] != grid[r-j-1][i]:
                    cf += 1

        return min(rf, cf) # Retorna oq precisou de menos alterações