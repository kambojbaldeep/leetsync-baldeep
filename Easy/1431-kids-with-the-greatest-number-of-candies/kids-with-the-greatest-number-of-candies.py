# Kids With the Greatest Number of Candies  (#1431)  —  Easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Runtime: 0 ms   |   Memory: 19.4 MB
# Language: Python3
# Synced: 2026-08-24 via LeetSync

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        ok = []
        for j in range(len(candies)):
            if candies[j] + extraCandies >= max_num:
                ok.append(True)
            else:
                ok.append(False)

        return ok
            
