class Solution:
    # def reverseWords(self, s: str) -> str:

    def removeExtraSpaces(self, s: str) -> str:
        slow, fast = 0, 0    # 
        s = list(s)
        while fast < len(s):
            if s[fast] != ' ':
                if slow != 0:         # 第一个单词之前不用留空格
                    s[slow] = ' '     # 每个单词之前留1个空格
                    slow += 1
                while fast < len(s) and s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            else:
                fast += 1
        return ''.join(s[:slow])

        
if __name__=="__main__":
    # 测试
    s = "   hello   world   "
    solution=Solution()
    res = solution.removeExtraSpaces(s)
    print(res)  # 输出: "hello world"