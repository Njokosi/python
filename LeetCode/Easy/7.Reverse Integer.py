class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])

        if result > 2 ** 31 - 1:
            return 0
        elif x < 0:
            return -result
        else:
            return result


n = int(input())
print(Solution().reverse(n))