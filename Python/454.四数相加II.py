from typing import List

# 一句话总结：
# 先用哈希表记录前两个数组所有和的出现次数，再遍历后两个数组，查找使四数之和为0的互补值，从而统计满足条件的组合个数。
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        records = {}  # key:a+b的数值, value:a+b数值出现的次数
        count = 0 # 满足四数相加等于0的组合个数

        for a in nums1:
            for b in nums2:
                if a+b in records:
                    records[a+b] += 1
                else:
                    records[a+b] = 1  # 如果还没有a+b这个键值，必须先初始化为1

        for c in nums3:
            for d in nums4:
                target = 0-(c+d)      # target：期望在records中找到的值
                if target in records: # 在records中寻找目标值
                    count += records[target] # 找到几个target就必须加上几个count

        return count


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    result = solution.fourSumCount(nums1, nums2, nums3, nums4)
    print(result)
