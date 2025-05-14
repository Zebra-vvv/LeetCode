from typing import List
import heapq # Python 中的堆操作模块

# 对元素的频率进行排序需要用到 map ，key就是元素值，value是元素出现的次数
# 题目只要求拿到前k个高频元素，所以不需要对所有元素进行排序，只需要维护一个大小为k的堆即可
# 这题需要用小顶堆，因为小顶堆的特性符合需要（不断把堆顶较小的元素pop出去，留下的反而是较大的元素）
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 利用map统计所有元素的出现频率
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        # 利用小顶堆heap来找出前k个高频元素
        heap = []  # 用List建立小顶堆即可，heapq模块可以帮忙维持堆结构
        for key, freq in map.items():
            # 将 map 中的一个元组 (freq, key) 添加到小顶堆 heap 中，并保持堆的性质，默认以元组的第一个元素进行排序，所以把freq放在前面
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])  # 只取元组的第2个元素，即 key
        # python 切片操作，其基本语法形式为 [start:stop:step]
        return result[::-1]  # 由于小顶堆的特性，需要逆序输出才是按照频率从高到低的顺序
    
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)


        