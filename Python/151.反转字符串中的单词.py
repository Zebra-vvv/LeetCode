class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 双指针反转单词之间的顺序
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串, 中间用空格连接
        return " ".join(words)
     
if __name__=="__main__":
    # 测试
    s = "the sky is blue"
    solution = Solution()
    res = solution.reverseWords(s)
    print(res)  # 输出: "hello world"