# 一句话总结：每隔 2k 个字符就反转前 k 个字符，最后不足 k 个或 2k 个的部分也按规则分别处理，整体实现字符串局部翻转。
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0, len(s_list), 2 * k):

            # 1. 每隔 2k 个字符的前 k 个字符进行反转
            # 2. 剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符
            # 1和2两种情况都可以用 if 中的代码执行(因为都是反转前k个)

            # 还没遍历到最后k个的时候, 统一反转前k个
            if i + k <= len(s_list):
                s_list[i:i+k] = reversed(s_list[i:i+k])

            else:
                # 3. 剩余字符少于 k 个，则将剩余字符全部反转。
                s_list[i:] = reversed(s_list[i:])
        # 将列表s_list中的所有元素连接成一个字符串, ''是连接字符串的分隔符，这里使用空字符串表示不需要分隔符
        return ''.join(s_list)


if __name__ == "__main__":
    str = "abcdefg"
    k = 2
    solution = Solution()
    result = solution.reverseStr(str, k)
    print(result)
