from typing import List
import bisect

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins = sorted(coins)
        prefix = [0 for i in range(len(coins) + 1)]
        vals = []
        for i, (l, r, c) in enumerate(coins):
            prefix[i+1] = prefix[i] + c*(r-l+1)
            vals.extend([l+k-1, r])
        vals = sorted(vals)
        # this is some magic lol 
        def f(x):
            i = bisect_right(coins, x, key=lambda x:x[0]) - 1
            if i < 0: return 0
            l, r, c = coins[i][0], coins[i][1], coins[i][2]
            return prefix[i] + (min(x, r) - l + 1)*c
        return max(f(r) - f(r-k) for r in vals)
