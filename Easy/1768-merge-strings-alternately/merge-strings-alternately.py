# Merge Strings Alternately  (#1768)  —  Easy
# https://leetcode.com/problems/merge-strings-alternately/
# Runtime: 48 ms   |   Memory: 19.2 MB
# Language: Python3
# Synced: 2026-08-21 via LeetSync

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = ""

        while i< len(word1) and j<len(word2):
            result += word1[i]
            result += word2[j]

            i +=1
            j+=1

        result += word1[i:]
        result += word2[j:]

        return result
        
        
