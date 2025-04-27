class Solution:
    def reverseWords(self, s: str) -> str:

        # 将字符串拆分为单词，并转换成List类型
        words = s.split() # words 是包含每个单词的 List
        # print(words)

        # 双指针反转单词之间的顺序(针对每个单词进行的操作)
        left = 0
        right = len(words) - 1
        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp

            # 不要老是忘记自增两个下标!!!
            left += 1
            right -= 1

        # 将列表转换成字符串, 中间用空格连接
        return ' '.join(words)
     
if __name__=="__main__":
    # 测试
    s = "   the sky is   blue   "
    solution = Solution()
    res = solution.reverseWords(s)
    print(res)  