from typing import List


# 一句话总结：贪心思路，计算每天的涨跌，只收获正利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):

            # 通过max函数和0比较，只累加 正利润 进result里面
            result += max(prices[i]-prices[i-1], 0)

        return result


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    res = solution.maxProfit(prices)
    print(res)
