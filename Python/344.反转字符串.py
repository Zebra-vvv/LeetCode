from typing import List

class Solution:
    def reverseString(self, str: List[str]) -> List[str]:
        left = 0
        right = len(str) - 1

        while left < right:
            temp = str[left]
            str[left] = str[right]
            str[right] = temp
            left += 1
            right -= 1
        return str

if __name__=="__main__":
    s = "hello"
    s_list = list(s)  # 将字符串转换为列表, 函数输入就是List
    solution = Solution()
    solution.reverseString(s_list)
    print(s_list)