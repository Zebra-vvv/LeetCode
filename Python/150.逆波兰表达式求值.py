from typing import List
from operator import add, sub, mul


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # 运算符映射表
        op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
        for token in tokens:

            # 是数字就入栈
            if token not in op_map:
                stack.append(int(token))

            # 是运算符就弹出两个数并计算后重新压回栈中
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num3 = op_map[token](num1, num2)
                stack.append(num3)
       
        return stack.pop()


if __name__ == "__main__":
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    result = solution.evalRPN(tokens)
    print(result)
