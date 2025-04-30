from typing import List

class Solution:
    def getNext(self, next:List[int], s:str):
        j = 0 # j是前缀末尾
        next[0] = 0
        for i in range(1, len(s)): # i是后缀末尾
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        next = [0] * len(s)
        self.getNext(next, s)
        l = next[len(s) - 1] # 字符串s中最长相等前后缀

        # 字符串存在相等前后缀 and 整个字符串能否被去掉最长相等前后缀的剩余部分整除
        if l > 0 and len(s) % (len(s) - l) == 0: 
            return True
        else:
            return False