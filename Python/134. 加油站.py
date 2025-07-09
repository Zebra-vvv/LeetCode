from typing import List


# 一句话总结：贪心，统计每站的盈余的油量，加入curSum，如果不够就尝试从下一个下标开始
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0  # 从当前位置开始，每站剩余的油量
        totalSum = 0  # 遍历一圈之后，最后剩余的油量
        start = 0  # 最后返回的结果，即开始的下标
        for i in range(len(gas)):
            curSum += gas[i]-cost[i]
            totalSum += gas[i]-cost[i]

            # 说明从当前位置开始，油量不够，需要以下一站为起点继续尝试
            if curSum < 0:
                start = i+1
                curSum = 0 # 从下一站开始，curSum也要重新开始统计

        return start if totalSum >= 0 else -1


if __name__ == "__main__":
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    res = solution.canCompleteCircuit(gas, cost)
    print(res)
