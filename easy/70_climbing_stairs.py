"""
https://leetcode.com/problems/climbing-stairs/description/

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        reach_pp = 1
        reach_p = 1

        for _ in range(2,n+1):
            reach_p, reach_pp = reach_p + reach_pp, reach_p
        return reach_p
