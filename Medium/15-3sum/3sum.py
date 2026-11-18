# 3Sum  (#15)  —  Medium
# https://leetcode.com/problems/3sum/
# Runtime: 3268 ms   |   Memory: 24.1 MB
# Language: Python3
# Synced: 2026-11-18 via LeetSync

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # A better approach

        n = len(nums)
        result = set()
        for i in range(0, n):
            my_set = set()
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])
                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])

        return [list(ans) for ans in result]
        
