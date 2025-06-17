from typing import List

# 一句话总结：模拟矩阵螺旋填数过程，按圈层从外到内依次赋值，最后处理中心点（若 n 为奇数）。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        nums = []
        for _ in range(n):
            nums.append([0] * n)

        startx, starty = 0, 0                        # 起始点的坐标
        loop, mid = n // 2, n // 2                   # 总共转的圈数、矩阵的中心点坐标（n为奇数时）
        count = 1                                    # 计数, 用来赋值
        for offset in range(1, loop + 1):            # 每转一圈，起始点横纵坐标偏移量加1
            for i in range(starty, n - offset):      # 从左至右, 填充不同的列(range是左闭右开的)
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):      # 从上至下, 填充不同的行, 所以行坐标变动, 用startx
                nums[i][n-offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左, 填充不同的列, 所以列坐标变动, 用starty
                nums[n-offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上, 填充不同的行
                nums[i][starty] = count
                count += 1

            # 每转一圈, 起始点横纵坐标都要加1
            startx += 1
            starty += 1

        # n为奇数时, 中心点需要额外赋值
        if n % 2 == 1:
            nums[mid][mid] = count

        return nums


if __name__ == "__main__":
    solution = Solution()
    n = 3
    res = solution.generateMatrix(3)
    print(res)
