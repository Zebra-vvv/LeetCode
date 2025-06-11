from typing import List

# 滑动窗口法（双指针法）
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = float('inf')  # min_len设置为无穷大, 确保下面min函数能找到最小值
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                
                # 刚刚加上一个右边界的数, 够了, 尝试从左边界去掉一个数, 看看还够不够
                sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    res = solution.minSubArrayLen(target, nums)
    print(res)
