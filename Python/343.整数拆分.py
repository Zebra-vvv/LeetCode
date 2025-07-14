# 一句话总结：动规，注意递推公式：(i - j) * j, dp[i - j] * j 这两种情况的含义
class Solution:
    def integerBreak(self, n):

        # dp数组定义：分拆数字i，可以得到的最大乘积为dp[i]
        dp = [0] * (n + 1)

        # dp数组初始化：dp[2]为1，因为当n=2时，只有一个切割方式1+1=2，乘积为1
        dp[2] = 1

        # 遍历顺序：从3开始计算，直到n
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):

                # 递推公式：计算切割点j和剩余部分(i-j)的乘积，并与之前的结果进行比较取较大值
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    n = 10
    res = solution.integerBreak(n)
    print(res)
