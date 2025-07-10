from typing import List


# 一句话总结：贪心，按照找零的思路直接模拟即可
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in range(len(bills)):
            
            # 遇到五块直接累加
            if bills[i] == 5:
                five += 1

            # 遇到十块，少一张五块，多一张十块
            elif bills[i] == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False

            elif bills[i] == 20:
                
                # 遇到二十块，优先找 十块+五块，因为 五块 比较珍贵（既可以处理10，又可以处理20）
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1

                # 如果没有十块，就看看有没有3张五块
                elif five >= 3:
                    five -= 3

                else:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    bills = [5, 5, 5, 10, 20]
    res = solution.lemonadeChange(bills)
    print(res)
