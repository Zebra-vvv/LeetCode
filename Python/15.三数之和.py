from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # 跳过重复的 i(因为要访问nums[i - 1], 为了防止越界, 所以必须判断 i > 0)
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:   
                    k -= 1 
                elif nums[i] + nums[j] + nums[k] < 0:
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