"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


def two_sum(numbers, target):
    i = 0
    while numbers:
        num1 = numbers[0]
        numbers = numbers[1:]
        for j in range(len(numbers)):
            target_sum = num1 + numbers[j]
            if target_sum == target:
                # print(f"Found at index {i} and {i + (j + 1)}")
                return [i, i + (j + 1)]
            else:
                continue

        i += 1


# nums = list(map(int, input().strip().split()))
# t = int(input())
nums = [3, 2, 4]
t = 6
print(two_sum(nums, t))
