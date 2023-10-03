"""
https://leetcode.com/problems/number-of-good-pairs/?envType=daily-question&envId=2023-10-03

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0



Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ans = 0
        for _, cnt in counts.items():
            ans += (cnt*(cnt - 1))>>1
        return ans

