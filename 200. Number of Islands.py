class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                islands += self.explore(grid, row, col, visited)
        
        return islands
    
    def explore(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0" or (row, col) in visited:
            return 0
        
        visited.add((row, col))

        self.explore(grid, row + 1, col, visited)
        self.explore(grid, row - 1, col, visited)
        self.explore(grid, row, col + 1, visited)
        self.explore(grid, row, col - 1, visited)

        return 1
