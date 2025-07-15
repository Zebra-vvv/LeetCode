class Solution:
    def numTrees(self, n: int) -> int:

        # dp[i]数组定义：1到i为节点组成的二叉搜索树的个数为dp[i]
        dp = [0] * (n+1)

        # dp数组初始化
        dp[0] = 1

        # 遍历顺序：从左到右，从头开始累加
        for i in range(1, n+1):
            for j in range(1, i+1):

                # 递推公式：以j为头结点，左子树节有j-1个节点，右子树有i-j个节点，左右子树相乘
                # 如果忘记了就再看一下B站视频
                dp[i] += dp[j-1] * dp[i-j]

        print(dp)
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    n = 3
    res = solution.numTrees(n)
    print(res)