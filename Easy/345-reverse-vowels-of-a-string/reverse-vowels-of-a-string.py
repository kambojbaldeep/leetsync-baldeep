# Reverse Vowels of a String  (#345)  —  Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Runtime: 7 ms   |   Memory: 20.6 MB
# Language: Python3
# Synced: 2026-08-24 via LeetSync

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"

        s = list(s)

        left = 0
        right = len(s) - 1

        while left<right:

            while left<right and s[left] not in vowels:
                left += 1

            while left<right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
