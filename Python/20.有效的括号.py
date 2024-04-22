class Solution:
    def isValid(self, s: str) -> bool:
        # python中可以使用列表来模拟栈的行为
        stack = []

        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")

            # 如果栈已经为空或者当前元素和栈顶元素不相等，说明匹配失败
            elif not stack or stack[-1] != item:
                return False
            # 当前元素和栈顶元素相等，弹出
            else:
                stack.pop()

        # 循环结束栈为空，匹配成功；循环结束栈内还有多余元素，匹配失败
        return True if not stack else False
    
if __name__=="__main__":
    s1 = "{[()]}"
    s2 = "{[])"
    solution = Solution()
    result1 = solution.isValid(s1)
    result2 = solution.isValid(s2)
    print(result1)
    print(result2)
            

