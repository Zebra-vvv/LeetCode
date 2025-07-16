from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp[j]：凑成总金额j的货币组合数为dp[j]
        dp = [0] * (amount + 1)

        # dp数组初始化
        dp[0] = 1

        # 遍历物品
        for i in range(len(coins)):

            # 遍历背包
            for j in range(coins[i], amount + 1):

                # 求装满背包有几种方法的递推公式都是这个
                # 看不懂的话就看这个视频的递推公式部分：https://www.bilibili.com/video/BV1o8411j73x?vd_source=5649d47eb899befde2cf3814bb161c55&spm_id_from=333.788.videopod.sections
                dp[j] += dp[j - coins[i]]

        return dp[amount]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    solution = Solution()
    res = solution.change(amount, coins)
    print(res)
