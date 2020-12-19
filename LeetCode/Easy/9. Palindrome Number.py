"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""


class Solution:
    def isPalindrome(self, num: int) -> bool:

        # Check if number is negative then it's not palindrome -1 != 1-
        if num < 0:
            return False

        # Check if the string number reversely is palindrome 121 == rev(121)
        elif str(num) == str(num)[::-1]:
            return True

        # Return false otherwise
        return False


n = 122
print(Solution().isPalindrome(n))
