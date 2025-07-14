# 一句话总结：动态规划思路，注意dp数组初始化的时候，第0行第0列都初始化为1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j]含义：第i行，第i列的位置，有多少种方法走到
        dp = [[0] * n for _ in range(m)]

        # dp数组初始化
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 遍历顺序：从左到右，从上到下
        for i in range(1, m):
            for j in range(1, n):

                # 递推公式
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回右下角单元格的唯一路径数
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solution = Solution()
    m = 3
    n = 7
    res = solution.uniquePaths(m, n)
    print(res)
