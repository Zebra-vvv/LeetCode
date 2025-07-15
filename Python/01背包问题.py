# 题目：https://kamacoder.com/problempage.php?pid=1046


# 依次读取三行（题目给的输入）
n, bagweight = map(int, input().split())  # 读入物品数量 n 和背包容量 bagweight
weight = list(map(int, input().split()))  # 读入每个物品的重量
value = list(map(int, input().split()))  # 读入每个物品的价值

# 定义二维 dp 数组，dp[i][j] 表示：前 i 件物品，在容量为 j 的背包中，能取得的最大价值
dp = [[0] * (bagweight + 1) for _ in range(n)]

# 初始化：只考虑第 0 个物品，在容量为 weight[0] ~ bagweight 的背包中可以放进去，价值为 value[0]
for j in range(weight[0], bagweight + 1):
    dp[0][j] = value[0]

# 开始动态规划，从第 1 件物品开始考虑
for i in range(1, n):
    for j in range(bagweight + 1):
        if j < weight[i]:
            # 当前背包容量不够放第 i 个物品，只能继承前 i-1 个物品的最优解
            dp[i][j] = dp[i - 1][j]
        else:
            # 两种情况取较大值：
            # 1. 不放第 i 个物品：dp[i - 1][j]
            # 2. 放第 i 个物品：dp[i - 1][j - weight[i]] + value[i]
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

# 输出最终结果：考虑前 n 个物品，背包容量为 bagweight 时的最大价值
print(dp[n - 1][bagweight])
