"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.


Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.

EXPLANATION:
https://www.geeksforgeeks.org/write-your-own-atoi/
"""


class Solution:
    def is_char_numeric(self, char):
        # This function checks if the character is numeric or not
        # We can alternatively use .isdecimal()
        if '0' <= char <= '9':
            return True
        return False

    def is_base_32(self, number):
        # Function checks if number is base 32 or not then return required result
        if -2 ** 31 <= number <= 2 ** 31 - 1:
            return number
        elif number < -2 ** 31:
            return -2 ** 31
        else:
            return 2 ** 31 - 1

    def myAtoi(self, text: str) -> int:

        # Remove the spaces at the beginning of the string
        text = text.lstrip()

        # If the string is empty return 0
        if len(text) == 0:
            return 0

        # Let's initialize the sign as positive, atoi number as 0
        atoi_number = 0
        sign = 1
        i = 0

        # If the number is negative then update the sign
        if text[0] == '-':
            sign = -1
            i += 1  # Then we go to the next character in the text
        if text[0] == '+':
            i += 1

        # If the first character is not numeric
        # if not is_char_numeric(text[i]):
        #     return 0

        # Extract the first word in the sentence
        first_text = text.split()[0]

        print(f"The first text: {first_text}")

        # If the number has decimal places then we get the integer part
        # first_text = first_text.split(".")[0]

        # if "".join(first_text.split(".")).isnumeric():

        # Iterate through the next characters of the te(if negative then i =1 else i =0)
        for j in range(i, len(first_text)):

            # Let's iterate through characters if not digit then break
            if not first_text[j].isdecimal():
                break
            # Note that ord('num') - ord('0') returns the difference between them which is int(num)
            atoi_number = atoi_number * 10 + (ord(text[j]) - ord('0'))
        # Multiply by the sign of the number
        atoi_number = sign * atoi_number

        # Check if number is base 32 else return (2^31 -1 or 2^31)
        atoi_number = self.is_base_32(atoi_number)

        return atoi_number


# t = input()
t1 = "42"
print(Solution().myAtoi(t1))

t2 = "   -42"
print(Solution().myAtoi(t2))

t3 = "4193 with words"
print(Solution().myAtoi(t3))

t4 = "words and 987"
print(Solution().myAtoi(t4))

t5 = "-91283472332"
print(Solution().myAtoi(t5))

t6 = "3.14159"
print(Solution().myAtoi(t6))

t7 = "+1"
print(Solution().myAtoi(t7))

t8 = " "
print(Solution().myAtoi(t8))

t9 = "  -0012a42"
print(Solution().myAtoi(t9))
