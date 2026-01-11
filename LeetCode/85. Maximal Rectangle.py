from lc import *
# ============================================================
# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# ============================================================


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        height = [0] * (m + 1)
        total = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            s = [0]
            for j in range(1, m + 1):
                while s and height[s[-1]] >= height[j]:
                    h = height[s.pop()]
                    w = j - 1 - (s[-1] if s else -1)
                    total = max(total, h * w)
                s.append(j)
        return total


test("""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
 
Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

 
Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.


""")
