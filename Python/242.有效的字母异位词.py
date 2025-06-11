# 一句话总结：
# 用长度为26的数组统计字母频次差值，判断两个字符串是否为字母异位词。原理是：s里每个字母 +1，t里每个字母 -1，最后看数组是否全为0。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        # 字符串可以直接这样遍历
        for i in s:
            # ord 函数用于获取字符的 ASCII 值, 因为是函数, 所以要用()
            # 在ASCII编码中，小写字母a的ASCII值是97，而字母'a'对应的数组索引应该是0。
            # 因此，如果我们用字母的ASCII值减去字母'a'的ASCII值，我们就可以得到字母在数组中的正确索引。
            # 例如：对于字母'a'，ord('a') - ord('a') 的结果是0，'a'在record确实应该在第一个位置
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)
