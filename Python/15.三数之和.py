from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不可能找到结果
            if nums[i] > 0:
                return result

            # 如果nums[i] == nums[i - 1], 那么这一轮的结果在上一轮都已收集了, 直接遍历下一轮
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 和上面的去重逻辑相同, 值和之前一轮的相等就不需要重复收集结果了
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)
