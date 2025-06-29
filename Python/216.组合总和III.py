from typing import List

# 和力扣77题思路几乎一样，多一个sum的判断
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(k, n, curSum=0, startIndex=1)
        return self.result

    def backtracking(self, k, n, curSum, startIndex):

        # 剪枝：当前的累加和已经大于目标和了，没有必要继续遍历了
        if curSum > n:
            return

        # 终止条件
        if len(self.path) == k:
            if curSum == n:
                self.result.append(self.path[:])
                return

        # 单层递归逻辑
        for i in range(startIndex, 9 - (k - len(self.path)) + 2): # 剪枝：后面的元素不够取到k个了，没有必要继续遍历了
            self.path.append(i)
            curSum += i
            self.backtracking(k, n, curSum, i+1)

            # 回溯
            curSum -= i
            self.path.pop()


if __name__ == "__main__":
    k=3
    n=9
    solution=Solution()
    res=solution.combinationSum3(k, n)
    print(res)
