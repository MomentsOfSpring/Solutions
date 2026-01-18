from lc import *
# ============================================================
# 1895. Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/
# ============================================================


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        total = 0

        p_rows = [[0] * m for _ in range(n)]
        p_cols = [[0] * m for _ in range(n)]
        p_md = [[0] * m for _ in range(n)]
        p_sd = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                p_rows[i][j] = grid[i][j] + (p_rows[i][j-1] if j > 0 else 0)
                p_cols[i][j] = grid[i][j] + (p_cols[i-1][j] if i > 0 else 0)
                p_md[i][j] = grid[i][j] + (p_md[i-1][j-1] if i > 0 and j > 0 else 0)
                p_sd[i][j] = grid[i][j] + (p_sd[i-1][j+1] if i > 0 and j < m - 1 else 0)


        for i in range(n):
            for j in range(m):
                for k in range(min(n - i, m - j) -1, -1, -1):
                    md = p_md[i + k][j + k] - (p_md[i-1][j-1] if i > 0 and j > 0 else 0)
                    sd = p_sd[i + k][j] - (p_sd[i-1][j + k + 1] if i > 0 and j+k+1 < m else 0)
                    if md != sd: 
                        continue
                    
                    valid = True
                    for r in range(i, i+k+1):
                        if p_rows[r][j+k] - (p_rows[r][j-1] if j > 0 else 0) != md:
                            valid = False 
                            break 
                    if not valid:
                        continue

                    
                    valid = True
                    for c in range(j, j+k+1):
                        if p_cols[i + k][c] - (p_cols[i-1][c] if i > 0 else 0) != md:
                            valid = False 
                            break 
                    if not valid:
                        continue

                    total = max(total, k + 1)
                    break
        return total



test("""
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.
 
Example 1:


Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:


Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106


""")
