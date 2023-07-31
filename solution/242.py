# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=1

s = "anagram"
t = "nagaram"

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram(s, t))
