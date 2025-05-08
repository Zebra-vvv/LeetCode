class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")
            elif i == "(":
                stack.append(")")
            
            # 循环内栈为空,说明元素被提前弹完了,右括号多了, return False
            # 当前元素和栈顶元素不匹配, 直接 return False
            elif not stack or i != stack[-1]:
                return False
            else:
                stack.pop()
        # 循环结束后,栈为空,说明匹配成功;  循环结束后,栈不为空
        return True if not stack else False