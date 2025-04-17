from typing import List

from typing import List

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
                record[value] = index
            index += 1
        return res
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result) 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []  # 存放函数最后返回的结果
        records = {}  # 存放遍历到的元素, key是nums中的元素, value是该元素在nums中的下标

        # enumerate函数用于创建迭代器, 同时返回元素的索引和值
        for index, value in enumerate(nums):
            if target-value in records:
                result.append(index)
                temp = records[target - value] # 从字典中取出另一个值的下标
                result.append(temp)
            else:
                records[value] = index # 将遍历的nums下标存入records字典中, nums元素值作为index
        return result


if __name__ == "__main__":
    nums = [2,7,11,15]
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