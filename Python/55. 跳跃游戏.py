from typing import List


# 一句话总结：for循环遍历数组，计算当前最远的覆盖范围，但是要注意当前位置有可能无法到达
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums)):

            # 当前位置无法到达，说明走到一半就走不下去了
            if i > max_index:
                return False

            # 能够到达当前位置，才有资格继续计算基于当前位置的覆盖范围
            max_index = max(max_index, i + nums[i])
        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    res = solution.canJump(nums)
    print(res)