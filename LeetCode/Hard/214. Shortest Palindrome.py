"""
https://leetcode.com/problems/shortest-palindrome/

Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.


Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""


class Solution:
    def find_longest_palindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longest_palindrome) >= j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    longest_palindrome = s[i:j]
        return longest_palindrome

    def find_first_palindrome(self, s: str, p: str) -> int:
        return s.find(p)

    def shortestPalindrome(self, s: str) -> str:
        palindrome = self.find_longest_palindrome(s)
        print(f"Palindrome: {palindrome}")
        # print(f"Palindrome first found: {self.find_first_palindrome(s, palindrome)}")
        first_palindrome_pos = self.find_first_palindrome(s, palindrome)
        print(f"Position of first palindrome: {first_palindrome_pos}")
        new_str = s.replace(palindrome, "", 1)
        rev_new_str = new_str[::-1]
        # print(new_str, rev_new_str)
        if first_palindrome_pos == 0:  # Palindrome is at the beginning
            return rev_new_str + s
        else:
            if first_palindrome_pos + len(palindrome) < len(s):  # Palindrome is found in the mid of string
                # Edit this
                extracted_str_end = s[(first_palindrome_pos + len(palindrome)):]
                print(f"Extracted end of string: {extracted_str_end}")
                palindrome = extracted_str_end[::-1] + palindrome + s
                return palindrome
            elif first_palindrome_pos + len(palindrome) == len(s):  # Palindrome is at the end of string
                if rev_new_str != new_str:
                    return palindrome + rev_new_str + s
                else:
                    if palindrome[-1] == s[0]:
                        return palindrome + palindrome
                    else:
                        return palindrome + s


# a = 'ambcd'
# a = 'abb'
a = "ababbbabbaba"
print(f"String: {a}")
print(Solution().shortestPalindrome(a))
print("ababbabbbababbbabbaba")