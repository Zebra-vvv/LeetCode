from typing import List


# 一句话总结：动规五部曲，目标是到第 len(cost) 阶（楼梯顶），它没有花费
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        # dp[i]：爬到第i阶台阶，已经花费了多少体力
        dp = [0] * (n + 1)

        # dp数组初始化，题意中从0或1开始，都不花费体力
        dp[0] = 0
        dp[1] = 0

        # 遍历顺序从前往后，因为后面依赖前面的状态
        for i in range(2, n+1):

            # 有两种爬上来的方法，取花费较小的
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        # print(dp)

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    cost = [10, 15, 20]
    res = solution.minCostClimbingStairs(cost)
    print(res)
