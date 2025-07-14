from typing import List


# 一句话总结：动规，和上一题的区别要注意：
# 1、初始化遇到障碍物就要停止循环
# 2、递推公式遇到障碍物就跳过，保持默认值0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 特判：起点或终点有障碍物，无法到达
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        # dp[i][j]含义：第i行，第i列的位置，有多少种方法走到
        dp = [[0] * n for _ in range(m)]

        # dp数组初始化：遇到障碍物时，直接退出循环，后面默认都是0
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):

                # 如果遇到障碍物，就不计算该位置了
                if obstacleGrid[i][j] == 1:
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print(res)
