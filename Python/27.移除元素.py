from typing import List

# 双指针法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex, fastIndex = 0, 0  # slowindex表示新数组下标, fastindex表示新数组的值
        size = len(nums)
        while fastIndex < size:
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1 # 只在找到新数组需要的元素时, slowIndex才会移动
            fastIndex += 1
        return slowIndex


if __name__ == "__main__":
    solution = Solution()
    nums= [0,1,2,2,3,0,4,2]
    val = 2
    res = solution.removeElement(nums, val)
    print(res)
