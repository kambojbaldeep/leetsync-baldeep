# Top K Frequent Elements  (#347)  —  Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 4 ms   |   Memory: 22.6 MB
# Language: Python3
# Synced: 2026-11-17 via LeetSync

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}

        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        topk = sorted(d, key = d.get, reverse = True)[:k]

        return topk
