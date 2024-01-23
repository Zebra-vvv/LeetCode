from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums: List[int] = [10, 20, 30, 40, 50, 60] # List要用方括号, 不要用花括号
    target = 30
    res = solution.search(nums, target)
    print(res)
