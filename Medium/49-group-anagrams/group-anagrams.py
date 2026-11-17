# Group Anagrams  (#49)  —  Medium
# https://leetcode.com/problems/group-anagrams/
# Runtime: 11 ms   |   Memory: 21.8 MB
# Language: Python3
# Synced: 2026-11-17 via LeetSync

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in dic:
                dic[key] = []

            dic[key].append(word)

        return list(dic.values())

        
