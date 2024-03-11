from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        return None
    
if __name__=="__main__":
    s = "hello"
    s_list = list(s)  # 将字符串转换为列表, 函数输入就是List
    solution=Solution()
    solution.reverseString(s_list)
    print(s_list)

    
    
