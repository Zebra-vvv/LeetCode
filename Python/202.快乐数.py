# 一句话总结：利用集合记录出现过的数，通过不断计算每位平方和，判断是否会循环或最终为1，从而判断是否为快乐数。
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果n在record中已经出现过，说明会陷入无限循环，不是快乐数
            if n in record:
                return False
            # 先判断是否已经出现过, 没出现过就把本轮计算的平方和加入到set中
            else:
                record.add(n)

    # 计算1次所有位的平方和, 调用一次get_sum函数
    def get_sum(self, n: int) -> int:
        sum = 0  # 每次调用, sum先清零
        while n != 0: # 判断是否算完了每一位数
            remainder = n % 10 # 取余, 取出最后一位（个位）
            sum += remainder ** 2 # 最后一位平方后加入sum
            quotient = n // 10 # 取商, 去掉最后一位（相当于“右移”）
            n = quotient # 如果只剩一位数，商会等于0，所以可以判断是否算完了
        return sum

if __name__ == "__main__":
    n = 19
    solution = Solution()
    result = solution.isHappy(n)
    print(result)
