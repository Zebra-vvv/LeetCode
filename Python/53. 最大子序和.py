from typing import List


# 一句话总结：当连续和为负数时，就抛弃，从下一个数开始重新计算，因为负数只会拖累后面的数
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')  # 全局最大的连续和
        sum = 0  # 每次遍历的连续和
        for i in range(len(nums)):
            sum += nums[i]

            # 更新result
            if sum > result:
                result = sum

            # 如果当前连续和已经是负数，就抛弃，重新开始计算
            if sum < 0:
                sum = 0

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = solution.maxSubArray(nums)
    print(res)
