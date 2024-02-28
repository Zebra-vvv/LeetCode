class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果n在record中出现过，说明会陷入无限循环，不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self, n: int) -> int:
        sum = 0  # 每次调用sum先清零
        while n != 0:
            quotient = n // 10 # 取商
            remainder = n % 10 # 取余数
            sum += remainder ** 2
            n = quotient # 商作为下一层循环的n
        return sum


if __name__ == "__main__":
    n = 19
    solution = Solution()
    result = solution.isHappy(n)
    print(result)
