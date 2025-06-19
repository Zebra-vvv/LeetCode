class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            # 栈不为空 且 当前元素等于栈顶元素
            if stack and i == stack[-1]: # 二刷又忘记了！既然要访问栈顶元素, 前面一定要判空!!!
                stack.pop() 
            
            # 不等的时候才需要append
            else:
                stack.append(i)
                
        # join() 是 Python 字符串对象的一个方法，用于将一个字符串列表合并成一个字符串，并用调用它的字符串作为“连接符”。
        return "".join(stack)
        

if __name__ == "__main__":
    s = "aabbca"
    solution = Solution()
    result = solution.removeDuplicates(s)
    print(result)


            