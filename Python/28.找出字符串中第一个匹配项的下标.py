from typing import List

# 一句话总结：
# KMP中getNext和strStr看似结构类似，其实前者是分析模式串自身结构，构建跳转表，后者是在匹配失败时用跳转表快速回退，它们虽然过程相似，但职责不同，前者为后者服务。
# 两者的共同核心是：通过回退 j 指针，避免重复比较，提高匹配效率。

# 刷题你就记住：getNext和strStr遇到匹配不相等的情况下，这样回退就行 j = next[j - 1]，不要纠结原因了

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
            next[i] = j # 每层for循环找到一个next[i]数组的值
    
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
                j = next[j - 1] # 需要回退的是模式串指针，表示从哪里开始重新匹配
            
            # 相等的情况
            if haystack[i] == needle[j]:
                j += 1

            # 模式串全部匹配成功
            if j == len(needle): # 这个条件才表示模式串最后一位也匹配成功了，然后+1
                return i - len(needle) + 1 # 回退一个模式串的长度, 就是开始的下标
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    result = solution.strStr(haystack, needle)
    print(f"在字符串 '{haystack}' 中找到子串 '{needle}' 的起始下标是: {result}")