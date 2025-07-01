from typing import List


# 一句话总结：基本和131.分隔回文串一样，就是把 判断是否回文 换成 判断ip是否合法
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.path = []
        self.result = []
        self.backtracking(s, startIndex=0)
        return self.result

    def backtracking(self, s, startIndex):

        # 剪枝：超过4段不合法
        if len(self.path) > 4:
            return

        # 终止条件
        if startIndex == len(s) and len(self.path) == 4:
            self.result.append('.'.join(self.path[:]))  # 注意需要拼成ip地址结构
            return

        # 单层递归逻辑
        for i in range(startIndex, len(s)):
            substring = s[startIndex:i+1]

            if not self.isvalid(substring):
                continue  # 如果非法就跳过

            self.path.append(substring)
            self.backtracking(s, i + 1)
            self.path.pop()

    def isvalid(self, s: str) -> bool:
        s_int = int(s)

        # 范围必须是0~255之间
        if s_int < 0 or s_int > 255:
            return False

        # 如果以0开头，但又不是0本身，非法
        if s.startswith('0') and s != '0':
            return False

        return True


if __name__ == "__main__":
    s = "25525511135"
    solution = Solution()
    res = solution.restoreIpAddresses(s)
    print(res)
