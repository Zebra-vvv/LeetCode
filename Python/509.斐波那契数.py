# 动规五部曲
class Solution:
    def fib(self, n: int) -> int:

        # 这里要特判，不然n=0时会报错
        if n <= 1:
            return n

        # dp[i]：第i个斐波那契数的值为dp[i]
        dp = [0] * (n+1)

        # dp数组初始化
        dp[0] = 0
        dp[1] = 1

        # 遍历顺序从前往后，因为后面依赖前面的状态
        for i in range(2, n+1):

            # 递推公式，斐波那契是直接给出的
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


if __name__ == "__main__":
    n = 30
    solution = Solution()
    res = solution.fib(n)
    print(res)
