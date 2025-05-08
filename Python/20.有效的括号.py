class Solution:
    def isValid(self, s: str) -> bool:
        # python中可以使用列表来模拟栈的行为
        stack = []

        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
 
            # 如果栈已经为空(右括号多了, 把栈内元素提前弹完了) 或者 当前元素和栈顶元素不相等，说明匹配失败
            elif not stack or i != stack[-1]:
                return False
            
            # 当前元素和栈顶元素相等，弹出
            else:
                stack.pop()

        # 循环结束栈为空，匹配成功；循环结束栈内还有多余元素(左括号多了），匹配失败
        return True if not stack else False
    
if __name__=="__main__":
    s1 = "{[()]}"
    s2 = "{[])"
    solution = Solution()
    result1 = solution.isValid(s1)
    result2 = solution.isValid(s2)
    print(result1)
    print(result2)
            

