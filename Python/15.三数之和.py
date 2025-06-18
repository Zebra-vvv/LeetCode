from typing import List

# 一句话总结：
# 这道题通过排序 + 双指针的方式解决三数之和问题：
# 先将数组排序，然后固定第一个数 nums[i]，接着用两个指针 j 和 k 在剩下的区间内查找满足 nums[i] + nums[j] + nums[k] == 0 的组合；
# 若和大于 0，说明右边太大，k--；若小于 0，说明左边太小，j++；
# 等于 0 时加入结果，并跳过重复的 j 和 k 元素以避免重复解。
# 整个过程通过去重和指针移动避免了暴力三重循环，时间复杂度优化为 O(n²)。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # 跳过重复的 i(因为要访问nums[i - 1], 为了防止越界, 所以必须判断 i > 0)
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:   
                    k -= 1 
                elif sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # 去重, 跳过重复的 j
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:  # 去重, 跳过重复的 k
                        k -= 1
        return res
        
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)