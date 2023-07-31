# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=1

s = "anagram"
t = "nagaram"


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagram(s, t))
