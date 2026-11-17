# Top K Frequent Elements  (#347)  —  Medium
# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 4 ms   |   Memory: 22.9 MB
# Language: Python3
# Synced: 2026-11-17 via LeetSync

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = Counter(nums)
        return heapq.nlargest(k, freqs, key=freqs.get)
