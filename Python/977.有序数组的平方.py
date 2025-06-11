from typing import List

# 暴力解法
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums

# 双指针法
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 因为题目给出的是递增序列, 平方后最大值肯定出现在两边, 从两边依次选择, 从大到小放入新数组即可
        left, right, i = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)  # 需要提前定义列表，存放结果
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:  # 左右边界进行对比，找出最大值
                res[i] = nums[right] ** 2
                right -= 1  # 右指针往左移动
            else:
                res[i] = nums[left] ** 2
                left += 1  # 左指针往右移动
            i -= 1  # 从后往前放
        return res


if __name__ == "__main__":
    solution = Solution2()
    nums: List[int] = [-4, -1, 0, 3, 10]
    res = solution.sortedSquares(nums)
    print(res)
