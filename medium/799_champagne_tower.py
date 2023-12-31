"""
https://leetcode.com/problems/champagne-tower/?envType=daily-question&envId=2023-09-24

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000



Constraints:

    0 <= poured <= 109
    0 <= query_glass <= query_row < 100

"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            for i in range(row):
                extra = prev[i] - 1
                if extra > 0:
                    cur_row[i] += (extra * 0.5)
                    cur_row[i+1] += (extra * 0.5)
            prev = cur_row
        
        return min(1, prev[query_glass])

