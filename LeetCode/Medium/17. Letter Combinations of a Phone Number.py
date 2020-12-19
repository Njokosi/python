"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
import itertools


def letter_combinations(nums: str) -> list:
    combs = {2: 'abc', 3: 'def', 4: 'ghi',
             5: 'jkl', 6: 'mno', 7: 'pqrs',
             8: 'tuv', 9: 'wxyz'}
    lists = []
    if nums:
        for num in nums:
            if int(num) in combs:
                lists.append(list(combs[int(num)]))

        output = list(itertools.product(*lists))
        final_output = []
        for val in output:
            final_output.append("".join(val))
        return final_output
    return lists


# n = input()
print(letter_combinations('23'))
