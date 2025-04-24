from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(len(nums)):

            # a的去重
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a + 1
            for b in range(a+1, len(nums)):   # 注意第二层循环的范围写法

                # b的去重不要遗漏了
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c = b + 1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum > target:
                        d -= 1
                    elif sum < target: 
                        c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1

                        # c和d的去重
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return res
        

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = solution.fourSum(nums, target)
    print(result)
