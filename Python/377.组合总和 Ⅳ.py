from typing import List


# 一句话总结：本题与动态规划：518.零钱兑换II (opens new window)就是一个鲜明的对比，一个是求排列，一个是求组合，遍历顺序完全不同。
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # dp[i]: 凑成目标正整数为i的排列个数为dp[i]
        dp = [0] * (target + 1)

        # 这题的dp[0]没有意义，仅仅为了递推公式的计算所以初始化为1
        dp[0] = 1

        # 如果求组合数就是外层for循环遍历物品，内层for遍历背包；如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        for i in range(1, target + 1):  # 遍历背包
            for j in range(len(nums)):  # 遍历物品
                if i - nums[j] >= 0:

                    # 求装满背包有多少种方法，都是这个递推公式
                    dp[i] += dp[i - nums[j]]
        return dp[target]
