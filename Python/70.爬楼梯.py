# 一句话总结：标准动规五部曲解题，注意n<=2的时候，要特判
class Solution:
    def climbStairs(self, n: int) -> int:

        # 注意特判
        if n <= 2:
            return n

        # dp[i]：第i阶台阶，有几种上来的方法
        dp = [0] * (n+1)

        # dp数组初始化
        dp[1] = 1
        dp[2] = 2

        # 遍历顺序从前往后，因为后面依赖前面的状态
        for i in range(3, n+1):

            # 第i阶只能由 第i-1阶迈一步上来，或者第i-2阶迈两步上来
            dp[i] = dp[i-1] + dp[i-2]

        # print(dp)
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    n = 5
    res = solution.climbStairs(n)
    print(res)
