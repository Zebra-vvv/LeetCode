from typing import List


# 一句话总结：贪心，维护当前覆盖范围和下一步的覆盖范围，每次走到当前覆盖范围的终点，说明必须要再走一步
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0  # 当前覆盖范围
        next = 0  # 下一步的最大覆盖范围
        step = 0  # 需要的步数

        if (len(nums) == 1):
            return 0

        for i in range(len(nums)):
            next = max(next, i+nums[i])
            if i == cur:
                step += 1
                cur = next
                if cur >= len(nums)-1:
                    break
        return step


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    res = solution.jump(nums)
    print(res)
