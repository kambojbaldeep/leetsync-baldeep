# Reverse Words in a String  (#151)  —  Medium
# https://leetcode.com/problems/reverse-words-in-a-string/
# Runtime: 2 ms   |   Memory: 19.3 MB
# Language: Python3
# Synced: 2026-08-24 via LeetSync

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
