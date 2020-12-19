"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""
# Solution 1

from collections import Counter


def make_anagrams(str1, str2):
    total = 0
    len_str1 = len(str1)
    len_str2 = len(str2)
    str_ctr = Counter(str1)

    for letter, repetition in str_ctr.items():
        if letter in str2:
            total += min(repetition, str2.count(letter))

    return len_str1 + len_str2 - (2 * total)


a = input()
b = input()

print(make_anagrams(a, b))

#  Solution 2

main_count = 0
total = 0
string1_set = set(a + b)
for i in range(len(string1_set)):
    count = a.count(list(string1_set)[i])
    count2 = b.count(list(string1_set)[i])
    if count > count2:
        main_count = count - count2
    elif count2 > count:
        main_count = count2 - count
    elif count2 == count:
        main_count = 0
    total = total + main_count
print(total)
