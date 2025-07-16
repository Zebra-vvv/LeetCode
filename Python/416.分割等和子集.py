from typing import List


# 一句话总结：动规，抽象为01背包问题：能否利用nums里的元素装满sum/2的背包
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # sum为奇数，肯定无法分割为两个相同的部分
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        # dp[j] 表示：容量（所能装的重量）为j的背包，所背的物品价值最大可以为dp[j]。

        # dp数组初始化
        dp = [0] * (target + 1)

        for num in nums:
            for j in range(target, num-1, -1):  # 每一个元素一定是不可重复放入，所以从大到小遍历

                # 递推公式：选和不选num，取价值更大的那个
                dp[j] = max(dp[j], dp[j-num] + num)

        if dp[-1] == target:
            return True
        else:
            return False


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    solution = Solution()
    res = solution.canPartition(nums)
    print(res)
