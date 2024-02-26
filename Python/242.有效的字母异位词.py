class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        # 字符串可以直接这样遍历
        for i in s:
            # ord 函数用于获取字符的 ASCII 值
            # 在ASCII编码中，小写字母a的ASCII值是97，而字母'a'对应的数组索引应该是0。
            # 因此，如果我们用字母的ASCII值减去字母'a'的ASCII值，我们就可以得到字母在数组中的正确索引。
            # 例如：对于字母'a'，ord('a') - ord('a') 的结果是0，'a'在record确实应该在第一个位置
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        result = all(count == 0 for count in record)
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)
