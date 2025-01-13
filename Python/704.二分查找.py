from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  
        while left <= right:
            # 两个/是python中的整数除法, 直接舍弃小数部分，保留整数部分
            # python中不需要防止溢出的写法
            mid = (left + right) // 2 
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12] 
    target = 9
    res = solution.search(nums, target)
    print(res)
