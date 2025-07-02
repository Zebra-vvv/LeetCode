from typing import List

# 一句话总结：贪心思路，大饼干尽量给大胃口，注意for循环一定用来遍历胃口，因为无论条件满不满足，胃口都要变动
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        # 先对两个数组进行排序
        g.sort()
        s.sort()

        j = len(s) - 1  # 从最大的饼干开始
        for i in range(len(g)-1, -1, -1):  # for循环从最大的胃口开始
           
            # 饼干用完了，防止数组越界
            if j < 0:
                break

            # 饼干能够满足胃口
            if s[j] >= g[i]:
                j -= 1
                count += 1

        return count


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    solution = Solution()
    res = solution.findContentChildren(g, s)
    print(res)
