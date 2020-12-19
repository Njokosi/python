"""
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


class Solution:
    def runningSum(self, numbers: list) -> list:
        # sums = []
        # for i in range(1, len(numbers) + 1):
        #     sums.append(sum(numbers[:i]))
        # return sums
        return [sum(numbers[:i]) for i in range(1, len(numbers) + 1)]


nums = [1, 1, 1, 1, 1]
print(Solution().runningSum(nums))

