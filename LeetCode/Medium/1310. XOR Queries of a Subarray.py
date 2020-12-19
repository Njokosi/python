"""
https://leetcode.com/problems/xor-queries-of-a-subarray

ASKED IN : AIRTEL

Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.


Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

"""
# Solution 1
import operator
from itertools import accumulate


class Solution:
    def xorQueries(self, arr, queries) -> list:
        record = [*accumulate(arr, operator.xor, initial=0)]
        for st, ed in queries:
            yield record[st] ^ record[ed + 1]


# Solution 2

class Solution:
    def xorQueries(self, arr, queries) -> list:
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1] ^ i)
        ans = []
        for i in queries:
            l, r = i
            ans.append(prefix[l] ^ prefix[r + 1])
        return ans


class Solution:
    def binary_to_decimal(self, num):
        # Function that converts binary number to decimal
        return int(num, 2)

    def xor_operation(self, num1, num2):
        # Function that performs the XOR operation

        # Different numbers are parsed
        num1 = bin(num1).replace("0b", "")
        num2 = bin(num2).replace("0b", "")

        # Get the lengths of the two numbers and append zeros in the beginning
        len_num1 = len(num1)
        len_num2 = len(num2)

        # The number of zeros to append at the end or beginning of string
        len_difference = abs(len_num2 - len_num1)

        if len_num1 < len_num2:
            num1 = "0" * len_difference + num1
        else:
            num2 = "0" * len_difference + num2

        # Storing the xor output of the two numbers
        output = ""

        # Do the XOR operation return without the "0b"
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                output += "1"
            else:
                output += "0"

        return output

    def xorQueries(self, numbers, queries):
        # Output with after the XOR operation
        ref_num = 0
        output = []
        total = 0

        # If the length of the list of numbers then return [0
        if len(numbers) <= 1:
            return [numbers[0]] * len(queries)

        else:
            for i in range(len(queries)):
                # Reference number for xor operation
                ref_num = numbers[queries[i][0]]
                # Perform the XOR operation between the reference number and the parsed number
                for j in range(min(queries[i]) + 1, max(queries[i]) + 1):
                    # NOTE THAT THE XOR OPERATION CAN BE PERFORMED WITH ^
                    # ref_num = self.binary_to_decimal(self.xor_operation(ref_num, numbers[j]))
                    ref_num = ref_num ^ numbers[j]
                output.append(ref_num)
        return output


nums = [1, 3, 4, 8]
qs = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(Solution().xorQueries(nums, qs))

nums = [4, 8, 2, 10]
qs = [[2, 3], [1, 3], [0, 0], [0, 3]]
print(Solution().xorQueries(nums, qs))

nums = [16]
qs = [[0, 0], [0, 0], [0, 0]]
print(Solution().xorQueries(nums, qs))
