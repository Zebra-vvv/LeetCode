# 一句话总结：从右向左比较相邻两位数字，一旦发现前一位大于后一位，就将前一位减 1，并标记从当前位置开始后续全部变为 9，以保证最终结果最大且单调递增。
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将整数转换为字符串
        strNum = str(n)

        # flag用来标记赋值9从哪里开始
        # 设置为字符串长度，为了防止第二个for循环在flag没有被赋值的情况下执行
        flag = len(strNum)

        # 从右往左遍历字符串
        for i in range(len(strNum) - 1, 0, -1):

            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                flag = i  # 更新flag的值，记录需要修改的位置

                # 将前一个字符减1，以保证递增性质（其余部分不变，直接拼接）
                strNum = strNum[:i - 1] + \
                    str(int(strNum[i - 1]) - 1) + strNum[i:]

        # 将flag位置及之后的字符都修改为9，以保证最大的递增数字（其余部分不变，直接拼接）
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]

        # 将最终的字符串转换回整数并返回
        return int(strNum)


if __name__ == "__main__":
    solution = Solution()
    n = 332
    res = solution.monotoneIncreasingDigits(n)
    print(res)
