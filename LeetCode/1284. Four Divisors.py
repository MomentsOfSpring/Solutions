# ============================================================
# 1284. Four Divisors
# https://leetcode.com/problems/four-divisors/
# ============================================================
from lc import *


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            seen = set()
            for divisor in range(1, int(num**0.5) + 1):
                if num % divisor == 0:
                    other = num // divisor
                    seen.add(other)
                    seen.add(divisor)
                    if len(seen) > 4:
                        break
            if len(seen) == 4:
                total += sum(seen)
        return total


test("""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
 
Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:

Input: nums = [21,21]
Output: 64

Example 3:

Input: nums = [1,2,3,4,5]
Output: 0

 
Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105

""")

