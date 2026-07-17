from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MAX = max(nums)

        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (MAX + 1)

        # cnt[g] = number of elements divisible by g
        for g in range(1, MAX + 1):
            for multiple in range(g, MAX + 1, g):
                cnt[g] += freq[multiple]

        # exact[g] = number of pairs with gcd exactly g
        exact = [0] * (MAX + 1)

        for g in range(MAX, 0, -1):
            c = cnt[g]
            exact[g] = c * (c - 1) // 2
            for multiple in range(g * 2, MAX + 1, g):
                exact[g] -= exact[multiple]

        prefix = []
        values = []
        total = 0

        for g in range(1, MAX + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans