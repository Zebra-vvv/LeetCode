from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        records = {}  # key:a+b的数值, value:a+b数值出现的次数

        for a in nums1:
            for b in nums2:
                if a+b in records:
                    records[a+b] += 1
                else:
                    records[a+b] = 1  # 如果还没有a+b这个键值，必须先初始化为1
        count = 0
        for c in nums3:
            for d in nums4:
                target = 0-(c+d)
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
