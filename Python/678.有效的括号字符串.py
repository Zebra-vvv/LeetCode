# 一句话总结：维护左右括号数量的可能上下限，遍历字符串动态调整区间范围，最终判断是否存在合法匹配。
class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0 # 最少可能的左括号数量（假设 * 都是右括号）
        high = 0 # 最多可能的左括号数量（假设 * 都是左括号）

        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == ')':
                low -= 1
                high -= 1
            else:  # i == '*'
                low -= 1    # * 当 ')'
                high += 1   # * 当 '('
            
            # 说明high被右括号疯狂-1，也就是右括号太多了，直接 False
            if high < 0:
                return False
            
            # 只是代表目前“最坏情况”太悲观，修正一下继续往下看。
            if low < 0:
                low = 0

        # 我们用 low 表示：
        # 在最坏的情况下（把所有的 * 都当成 )），我们最少还有多少个左括号没被匹配。
        # 如果 low == 0：
        # 说明即便是最糟糕的假设，我们也成功让所有左括号匹配上了（也包括处理掉了 *），一切都刚刚好 ✅
        # 如果 low > 0：
        # 那代表：有些左括号是无论怎么用 * 都匹配不掉的，也就是说，这个字符串不合法 ❌
        return low == 0

if __name__ == "__main__":
    str = "(*)"
    solution = Solution()
    res = solution.checkValidString(str)
    print(res)