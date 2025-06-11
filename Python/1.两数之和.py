from typing import List

# 一句话总结:使用map记录元素及其下标，在遍历数组时快速查找目标差值是否已出现，从而在一次遍历中找到两数之和等于目标值的索引对。
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        record = {} # 存放遍历到的元素, key是nums中的元素, value是该元素在nums中的下标
        res = [] # 存放函数最后返回的结果
        index = 0 # 自己维护下标, 循环1次, 下标自增
        for value in nums:
            if target-value in record:
                res.append(index)
                res.append(record[target-value])
            else:
                # 把当前值的下标存到map里去，方便查询
                record[value] = index
            index += 1
        return res
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result) 

"""
模拟算法过程:
index     value      target-value       records                  result
0           2             7              {2:0}                     []
1           7             2              {2:0}                    [1,0]
2          11            -2              {2:0, 11:2}              [1,0]
3          15            -6              {2:0, 11:2, 15:3}        [1,0]
""" 