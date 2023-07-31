# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=1

s = "anagram"
t = "nagaram"


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


print(isAnagram(s, t))
