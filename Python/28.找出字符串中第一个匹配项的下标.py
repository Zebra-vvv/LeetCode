from typing import List

# 其实就是KMP算法
class Solution:

    # 这种方式求出来的next数组就是 原始前缀表(没有整体减1或者整体右移)
    def getNext(self, next:List[int], s:str):

        j = 0 # j是前缀末尾的下标
        next[0] = 0

        # i是后缀末尾的下标
        for i in range(1, len(s)): 

            # 前后缀不相同的情况, 需要连续回退, 故需要用 while 而不是 if
            while j > 0 and s[i] != s[j]:
                j = next[j - 1] # j连续回退到前一位对应的next数组值
            if s[i] == s[j]:
                j += 1
            next[i] = j
    
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0  # j是模式串的指针, 注意这里初始化j为0

        # i 是文本串的指针, 此时i从0开始, 因为两者都要从头开始匹配
        for i in range(len(haystack)):

            # 遇到不匹配的字符, 需要连续回退
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            
            # 相等的情况
            if haystack[i] == needle[j]:
                j += 1

            # 模式串全部匹配成功
            if j == len(needle):
                return i - len(needle) + 1
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    result = solution.strStr(haystack, needle)
    print(f"在字符串 '{haystack}' 中找到子串 '{needle}' 的起始下标是: {result}")