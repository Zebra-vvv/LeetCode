from typing import List

# 一句话总结：使用栈模拟逆波兰表达式的计算过程，遇数字入栈，遇运算符弹出栈顶两个元素运算后再压入，注意操作数顺序与除法取整规则。
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for i in tokens:

            # 遇到数字就无脑入栈
            if i not in op:
                stack.append(int(i)) # 注意要把字符串转成整数

            # 遇到操作符, 就从栈顶弹出两个进行计算, 并将计算结果压回栈中
            else:
                a = stack.pop()
                b = stack.pop()

                # 这里要注意a和b的顺序, b是后面的
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                elif i == '/':
                    stack.append(int(b / a)) # 向0取整(直接去掉小数部分, 向0靠近)
        return stack.pop()


if __name__ == "__main__":
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    result = solution.evalRPN(tokens)
    print(result)
