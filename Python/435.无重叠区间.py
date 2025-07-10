from typing import List


# 一句话总结：贪心，一个重叠区域至少移除一个区间，如果有更多重叠，则需要移除更多的区间
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) == 0:
            return 0

        # 按左边界升序排列
        intervals.sort(key=lambda x: x[0])

        result = 0

        for i in range(1, len(intervals)):

            # 有重叠
            if intervals[i][0] < intervals[i-1][1]:

                # 一个重叠区域，至少移除一个区间才能解决
                result += 1

                # 更新右边界，判断下一个区间是否继续和当前重叠区域继续重叠
                # 如果继续重叠，需要result += 1，相当于需要移除2个区间才能解决这个重叠区域
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])

        return result


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    res = solution.eraseOverlapIntervals(intervals)
    print(res)
