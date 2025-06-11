from typing import List

# 线性查找 O(m × n)
class Solution1:
    def intersection (self, nums1:List[int], nums2:List[int]) -> List[int]:
        result = set()
        for i in nums1:
            if i in nums2:
                result.add(i)
        return list(result)
    
# 哈希查找 O(m + n)
# 一句话总结：“用集合去重并查找两个数组的公共元素。”利用哈希集合快速查找，时间复杂度优于暴力法。
class Solution2:
    def intersection (self, nums1:List[int], nums2:List[int]) -> List[int]:
       
        result_set = set()
        
        # 先把nums1的元素放到set中去, 在set中查找元素的时间复杂度是 O(1), 因为它是基于哈希表实现的
        set1 = set()
        for i in nums1:
            set1.add(i)

        # 在set1中寻找nums2元素
        for i in nums2:
            if i in set1:
                result_set.add(i)

        # 函数要求返回值为列表, 将集合转换为列表
        result_list = list(result_set)  
        return result_list

if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 3]
    solution = Solution2()
    res = solution.intersection(nums1, nums2)
    print(res)

