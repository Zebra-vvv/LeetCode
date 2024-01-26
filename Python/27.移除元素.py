from typing import List


# 暴力解法
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:  # 不是i <= l, i = l 是没有意义的, 超出数组了
            if nums[i] == val:
                for j in range(i + 1, l):  # range是左闭右开的
                    nums[j-1] = nums[j]
                i -= 1  # 如果遇到相等的情况, i需要回退
                l -= 1
            i += 1
        return l

# 双指针法
class Solution2:
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
    solution = Solution2()
    nums: List[int] = [1, 2, 2, 3, 4]
    val = 2
    res = solution.removeElement(nums, val)
    print(res)
