class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            # 栈不为空且当前元素等于栈顶元素
            if stack and item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
                
        # 将栈中剩余字符串拼接并返回
        return "".join(stack)
        

if __name__ == "__main__":
    s = "aabbca"
    solution = Solution()
    result = solution.removeDuplicates(s)
    print(result)


            