"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:
Input: "aeiou"
Output: ""
"""
import re

#  Solution 1


class Solution:
    def removeVowels(self, text: str) -> str:
        return re.sub("[aeiou]", "", text)

# Solution 2


def remove_vowels(text):
    result = ""
    for i in range(len(text)):
        if text[i] not in "aeiou":
            result += text[i]
    return result


msg = "hello"
print(Solution().removeVowels(msg))

print(remove_vowels(msg))
