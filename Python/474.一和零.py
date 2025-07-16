from typing import List


# 一句话总结：动规
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为dp[i][j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 创建二维动态规划数组，初始化为0
        
        # 遍历物品
        for s in strs:
            ones = s.count('1')  # 统计字符串中1的个数
            zeros = s.count('0')  # 统计字符串中0的个数
            
            # 遍历背包容量且从后向前遍历
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    
                    # 递推公式：
                    # 不选当前字符串：上一轮的 dp[i][j] 保持不变
                    # 选当前字符串 s（需要 zeros 个 0 和 ones 个 1）：从状态 dp[i - zeros][j - ones] 走过来，再加上当前这个字符串，总数 +1
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1) 
        
        return dp[m][n]