from typing import List


# 一句话总结：贪心思想，通过计算 curdiff 和 prediff 来判断，注意考虑几个边界情况
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # 数组长度为0或1，特殊处理
        if len(nums) <= 1:
            return len(nums)

        prediff = 0  # 特殊处理：在只有2个元素的时候，相当于在数组最前面延伸了一个平坡
        count = 1  # 默认最后一个元素为一个摆动

        # for循环最后一个元素不用遍历
        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]

            # prediff要带上等号，因为要考虑平坡的情况
            if (prediff >= 0 and curdiff < 0) or (prediff <= 0 and curdiff > 0):
                count += 1

                # 只在摆动变化时更新prediff
                prediff = curdiff

        return count


if __name__ == "__main__":
    nums = [1, 7, 4, 9, 2, 5]
    solution = Solution()
    res = solution.wiggleMaxLength(nums)
    print(res)
