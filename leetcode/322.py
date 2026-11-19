from typing import List
import queue


class Solution:
    def __init__(self):
        self.inf = 10**9
    def solve(coins, depth, current, amount, memo):
        """ BFS search for the minimum number of coins to make up the amount
        """
        q = queue.Queue()
        q.put((depth, current))
        while not q.empty():
            depth, current = q.get()
            for i in range(len(coins)):
                next_current = current + coins[i]
                if next_current <= amount and next_current not in memo:
                    memo[next_current] = depth+1
                    q.put((depth+1, next_current))
    def dp_solve(self, coins,amount):
        """ F(S) = min(F(S), F(S - C_i) + 1)
        Optimal ubstructure
        """
        dp = [self.inf] * (amount + 1)
        dp[0] = 0
        for curr_sum in range(1, amount + 1):
            for coin in coins:
                if curr_sum - coin >= 0:
                    dp[curr_sum] = min(dp[curr_sum], dp[curr_sum - coin] + 1)

        return dp[amount] if dp[amount] != self.inf else -1 

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp_solve(coins, amount)


if __name__ == '__main__':
    s = Solution()
    testcases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        # amount 0 needs no coins, whatever the coins are
        ([5], 0, 0),
        ([1], 1, 1),
        ([1], 2, 2),
        # every coin is bigger than the amount
        ([2], 1, -1),
        ([2], 4, 2),
        # greedy (take the biggest coin first) gives 4+1+1 = 3 coins, but 3+3 = 2
        ([1, 3, 4], 6, 2),
        # coins not given in sorted order
        ([2, 5, 10, 1], 27, 4),
        ([3, 5], 7, -1),
        ([3, 5], 11, 3),
        ([186, 419, 83, 408], 6249, 20),
        ([3, 7, 405, 436], 8839, 25),
        ([474, 83, 404, 3], 264, 8),
        # only even coins can never make an odd amount
        ([2], 9999, -1),
        (list(range(2, 25, 2)), 9999, -1),
        # coin values up to 2^31 - 1: watch for overflow / huge array sizes
        ([2**31 - 1], 10**4, -1),
        ([1, 2**31 - 1], 3, 3),
        # Max amount (10^4): a plain recursive search without memoization will be too slow
        ([1], 10**4, 10**4),
        ([1, 2, 5], 10**4, 2000),
        ([7, 11], 10**4, 912),
    ]
    for i, (coins, amount, want) in enumerate(testcases):
        got = s.coinChange(coins, amount)
        if got != want:
            print('Test {}: got != want, {} != {}'.format(i, got, want))
        else:
            print('Test {}: passed'.format(i))
