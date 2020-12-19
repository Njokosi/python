"""
DESCRIPTION:
https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/

The idea is to represent N as a sequence of length L+1 as:
N = a + (a+1) + (a+2) + .. + (a+L)
=> N = (L+1)*a + (L*(L+1))/2
=> a = (N- L*(L+1)/2)/(L+1)
We substitute the values of L starting from 1 till L*(L+1)/2 < N
If we get 'a' as a natural number then the solution should be counted.

"""


def countConsecutive(N):
    # constraint on values of L gives us the
    # time Complexity as O(N^0.5)

    count = 1  # We start count as 1, because number itself is included
    L = 1
    while L * (L + 1) < 2 * N:
        a = (1.0 * N - (L * (L + 1)) / 2) / (L + 1)
        if a - int(a) == 0.0:
            count += 1
        L += 1
    return count


N = 5
print(countConsecutive(N))
