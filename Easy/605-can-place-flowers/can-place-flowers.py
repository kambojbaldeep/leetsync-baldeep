# Can Place Flowers  (#605)  —  Easy
# https://leetcode.com/problems/can-place-flowers/
# Runtime: 11 ms   |   Memory: 19.6 MB
# Language: Python3
# Synced: 2026-08-24 via LeetSync

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left_empty = (i == 0 or flowerbed[i-1] == 0)
                right_empty = (i == (len(flowerbed)- 1) or flowerbed[i+1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

        return n<= 0
