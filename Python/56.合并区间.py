from typing import List


# 一句话总结：维护一个合并结果集合 result，每次和当前正在处理的区间 intervals[i] 比较，如果发现有重叠，就更新 result 中最后一个合并区间的右边界。
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        # 按照左边界升序排列
        intervals.sort(key=lambda x: x[0])

        # 第1个元素直接添加进来
        result.append(intervals[0])

        # 因为第1个元素已经添加到result中，所以i从1开始遍历
        for i in range(1, len(intervals)):

            # 有重叠
            if result[-1][1] >= intervals[i][0]:

                # 有重叠，就更新结果集最后一个区间的右边界
                result[-1][1] = max(result[-1][1], intervals[i][1])

            else:
                # 一旦没有重叠，就会在result中新加入一个元素
                result.append(intervals[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = solution.merge(intervals)
    print(res)