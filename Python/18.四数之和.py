from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for a in range(len(nums)):

            # 如果nums[i] == nums[i - 1], 那么这一轮的结果在上一轮都已收集了, 直接遍历下一轮
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a+1, len(nums)):

                if b > a+1 and nums[b] == nums[b - 1]:
                    continue

                left, right = b + 1, len(nums) - 1
                while left < right:
                    sum = nums[a] + nums[b] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        result.append([nums[a], nums[b], nums[left], nums[right]])

                        # 和上面的去重逻辑相同, 值和之前一轮的相等就不需要重复收集结果了
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        right -= 1
                        left += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = solution.fourSum(nums, target)
    print(result)
