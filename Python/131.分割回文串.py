from typing import List

# 一句话总结：切割问题其实和组合问题是一样的，就是要搞清楚子串的范围其实就是[startIndex, i]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.path = []
        self.result = []
        self.backtracking(s, startIndex=0)
        return self.result

    def backtracking(self, s, startIndex):

        # 终止条件
        if startIndex == len(s):
            self.result.append(self.path[:])

        # 单层递归逻辑
        for i in range(startIndex, len(s)):

            # 子串范围其实就是[startIndex, i]，但是python切片操作是左闭右开，所以i+1
            substring = s[startIndex:i+1]

            if not self.isPalindrome(substring):
                continue  # 不是回文就跳过

            self.path.append(substring)  # 把当前切割的子串加入path
            self.backtracking(s, i+1)
            self.path.pop()

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    res = solution.partition(s)
    print(res)
