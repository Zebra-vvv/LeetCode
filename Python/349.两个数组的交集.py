from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        result_set = set()
        for i in nums1:
            set1.add(i)
        for i in nums2:
            if i in set1:
                result_set.add(i)
        result_list = list(result_set)  # 函数要求返回值为列表, 将集合转换为列表
        return result_list


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 3]
    solution = Solution()
    result = solution.intersection(nums1, nums2)
    print(result)
