from typing import List


# 一句话总结：贪心，优先把所有负数取反，如果所有负数取反之后，k还没消耗完，就对最小的正数继续取反
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        # 先把负数从前往后取反
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        # 如果还有剩下的 k 且为奇数，反转最小的那个正数
        # 如果 剩余的 k 是偶数，对任何数做 k 次反转后，最终结果等价于没有反转，所以不需要额外操作
        if k % 2 == 1:

            # 负数反转之后，需要重新排序
            nums.sort()

            nums[0] = -nums[0]

        return sum(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [2, -3, -1, 5, -4]
    k = 2
    res = solution.largestSumAfterKNegations(nums, k)
    print(res)
