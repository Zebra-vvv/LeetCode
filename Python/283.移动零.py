from typing import List

# 一句话总结：双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    
        # j 指针表示当前非零元素应该存放的位置
        j = 0

        # 遍历数组，找出所有非零元素，按顺序往前放
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]  # 把非零元素移到前面
                j += 1             # 移动写入指针

        # 将剩余位置补 0
        while j < len(nums):
            nums[j] = 0
            j += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)
