"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

EXPLANATIONS:
https://www.geeksforgeeks.org/print-concatenation-of-zig-zag-string-form-in-n-rows/

"""


class Solution:
    def convert(self, text: str, n: int) -> str:

        # In case we have one row
        if n == 1:
            return text

        # Length of the string
        text_length = len(text)

        #  Create an array of string for n rows
        arr = ['' for i in range(n)]

        # Initialize the index for array of strings arr[]
        row = 0

        # Traverse through the given string
        for i in range(text_length):
            arr[row] += text[i]

            # If the last row is reached
            if row == n - 1:
                down = False

            #  If the first row is reached then direction is down
            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        return ''.join(arr)


t = input()
num = int(input())
print(Solution().convert(t, num))
