# 题目：https://kamacoder.com/problempage.php?pid=1052

def complete_knapsack(n, bag_weight, items):
    weight = [item[0] for item in items]
    value = [item[1] for item in items]

    # 初始化二维 dp 数组
    dp = [[0] * (bag_weight + 1) for _ in range(n)]

    # 初始化第 0 个物品：完全背包，注意是可重复选择
    for j in range(weight[0], bag_weight + 1):
        dp[0][j] = dp[0][j - weight[0]] + value[0]

    # 填表
    for i in range(1, n):  # 遍历物品
        for j in range(bag_weight + 1):  # 遍历容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                # 完全背包：可以选多次，所以这里是 dp[i][j - weight[i]]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i]] + value[i])

    return dp[n - 1][bag_weight]

# 示例输入读取
if __name__ == "__main__":
    n, bag_weight = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    result = complete_knapsack(n, bag_weight, items)
    print(result)
