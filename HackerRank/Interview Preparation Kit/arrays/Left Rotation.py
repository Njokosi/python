"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:


"""

n, d = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

# Solution 1


def left_rotation(numbers, rotations):
    new_array = [0 for i in range(len(numbers))]
    print(new_array)
    for i in range(len(numbers)):
        new_pos = i - rotations
        new_array[new_pos] = numbers[i]
    print(' '.join(map(str, new_array)))


left_rotation(nums, d)

# Solution 2


def array_left_rotation(a, n, k):
    a = list(a)
    return a[k:] + a[:k]


answer = array_left_rotation(nums, n, d)
print(*answer, sep=' ')
