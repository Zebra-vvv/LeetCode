# 对元素的频率进行排序需要用到 map ，key就是元素值,value是元素出现的次数
# 题目只要求拿到前k个高频元素，所以不需要对所有元素进行排序，只需要维护一个大小为k的堆即可
# 必须维护小顶堆而不是大顶堆，因为遍历所有元素时，新加入元素会不断弹出最小的堆顶元素，最后剩下的就是最大的k个元素

from typing import List

# Python 中的一个模块，提供了对堆数据结构的支持
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 统计频率
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, frep in freq_map.items():
            # 将 freq_map 中的一个元组 (freq, key) 添加到堆 pri_que 中，并保持堆的性质，以元组的第一个元素进行排序，默认就是小顶堆
            heapq.heappush(pri_que, (frep, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        result = []
        while pri_que:
            result.append(heapq.heappop(pri_que)[1])  # 只取元组的第二个元素，即 key
        # python 切片操作，其基本语法形式为 [start:stop:step]
        return result[::-1]  # 由于小顶堆的特性，需要逆序输出才是按照频率从高到低的顺序
    
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)


        