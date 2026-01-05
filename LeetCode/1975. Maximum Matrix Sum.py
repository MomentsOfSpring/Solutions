from lc import *
# ============================================================
# 1975. Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/
# ============================================================


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        absmin = float("inf")
        ideal, negnums = 0, 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                ideal += abs(num)
                negnums += 1 if num < 0 else 0

                if abs(num) < absmin:
                    absmin = min(absmin, abs(num))

        return ideal if negnums % 2 == 0 else ideal - (absmin * 2)


test("""
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
 
Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

 
Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105

""")
