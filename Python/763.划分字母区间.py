from typing import List


# 一句话总结：先统计s中每个字母的最远出现位置，存在hash中，再去遍历分隔
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # 统计每个字母的最远出现位置
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i

        result = []

        left, right = 0, 0
        for i in range(len(s)):

            # 一直维护当前分隔段的最远右边界
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:

                # 一旦到达右边界，说明可以分隔了
                result.append(right-left+1)
                left = i+1
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "ababcbacadefegdehijhklij"
    res = solution.partitionLabels(s)
    print(res)
