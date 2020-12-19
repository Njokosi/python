"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Solution 1


def find_common_prefix(strings):
    prefix = ""
    # Refer zipping.py
    for x in zip(*strings):
        if len(set(x)) == 1:
            prefix += x[0]
        else:
            break
    return prefix


class Solution:
    # This function finds the common prefix between two texts
    def find_common_prefix(self, str1: str, str2: str) -> str:

        # Common prefix between the two strings to be returned
        common_prefix = ''

        # Traverse through two strings, break after reaching the length of the shortest string
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                break
            common_prefix += str1[i]
            i += 1
            j += 1

        return common_prefix

    def longestCommonPrefix(self, texts: list) -> str:

        # Length of the lists of the texts
        total_texts = len(texts)

        # Pick the reference text in the list of texts
        if total_texts < 1:
            return ''

        reference_text = texts[0]

        if total_texts == 1:
            return reference_text

        else:

            # Compare with the reference text with other texts characters
            for i in range(1, total_texts):
                reference_text = self.find_common_prefix(reference_text, texts[i])

        return reference_text

    # Solution 2


# print(Solution().find_common_prefix('flower', 'flow'))

s1 = ["a"]
print(Solution().longestCommonPrefix(s1))

s1 = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(s1))

s1 = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(s1))
