from typing import List

# 双指针法
# 一句话总结：快慢指针遍历数组，将不等于目标值的元素放到slow里面，实现原地删除并返回新长度。
class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums): # while条件
            if nums[fast] != val: 
                nums[slow] = nums[fast]
                slow += 1 # slow 只取需要的元素
            fast += 1 # fast 满不满足都递增
        return slow


if __name__ == "__main__":
    solution = Solution()
    nums= [0,1,2,2,3,0,4,2]
    val = 2
    res = solution.removeElement(nums, val)
    print(res)
