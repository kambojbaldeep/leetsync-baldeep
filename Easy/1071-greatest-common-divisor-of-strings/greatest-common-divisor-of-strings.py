# Greatest Common Divisor of Strings  (#1071)  —  Easy
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Runtime: 1 ms   |   Memory: 19.3 MB
# Language: Python3
# Synced: 2026-08-19 via LeetSync

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
