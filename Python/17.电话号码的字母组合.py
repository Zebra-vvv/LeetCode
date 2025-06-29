from typing import List


# 使用回溯法逐位构造数字映射的字母组合路径，利用递归探索所有可能结果，并在终止时将路径拼接成字符串加入结果集。
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []
        
        self.path = []
        self.result = []
        self.backtracking(digits, index=0)
        return self.result

    def backtracking(self, digits, index):

        # 终止条件
        if index == len(digits):
            self.result.append("".join(self.path))  # 注意join的拼接方法
            return

        # 单层递归逻辑
        digit = digits[index]  # 取当前遍历的数字
        letter = self.letterMap[digit]  # 取数字映射的字母
        for i in range(len(letter)):
            self.path.append(letter[i])
            self.backtracking(digits, index + 1)

            # 回溯
            self.path.pop()


if __name__ == "__main__":
    digits = "23"
    solution = Solution()
    res = solution.letterCombinations(digits)
    print(res)
