from typing import List


# 一句话总结：动规，关键是理解下面这个推导

# 既然为target，那么就一定有 left组合 - right组合 = target。
# left + right = sum，而sum是固定的。right = sum - left
# left - (sum - left) = target 推导出 left = (target + sum)/2 。
# target是固定的，sum是固定的，left就可以求出来。
# 此时问题就是在集合nums中找出和为left的组合。
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和

        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案

        target_sum = (target + total_sum) // 2  # 目标和
        dp = [0] * (target_sum + 1)  # 创建动态规划数组，初始化为0
        dp[0] = 1  # 当目标和为0时，只有一种方案，即什么都不选
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]  # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum]  # 返回达到目标和的方案数


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    solution = Solution()
    res = solution.findTargetSumWays(nums, target)
    print(res)
