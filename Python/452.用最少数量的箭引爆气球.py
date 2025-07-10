from typing import List


# 一句话总结：贪心，尽可能把重叠的气球一起射爆，先对左边界进行排序，根据右边界判断是否重叠
class Solution:
    def findMinArrowShots(self, points: List[List[int]]):
        if len(points) == 0:
            return 0

        # 按左边界升序排列
        points.sort(key=lambda x: x[0])

        # points不为空，至少需要1根箭
        arrow = 1

        for i in range(1, len(points)):

            # 两个气球不挨着
            if points[i][0] > points[i-1][1]:
                arrow += 1

            else:
                # 取最小右边界，可以用来判断下一个气球是不是也可以一起带着射爆
                points[i][1] = min(points[i - 1][1], points[i][1])
        return arrow


if __name__ == "__main__":
    solution = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    res = solution.findMinArrowShots(points)
    print(res)
