from typing import List

# 一句话总结：回溯模板，注意这道题result加入时的处理方式，isValid不需要校验行方向
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # 初始化棋盘
        self.chessboard = [['.'] * n for _ in range(n)]

        self.result = []
        self.backtracking(n, row=0)
        return self.result

    def backtracking(self, n, row):

        # 终止条件：如果已经放满 n 行，表示找到一个解
        if row == n:

            # 拼接成题目要求的格式，并且完成了深拷贝，不会被后续回溯操作影响
            board = ["".join(row) for row in self.chessboard]
            self.result.append(board)

            return

        # 单层递归逻辑
        for col in range(n):
            if self.isValid(row, col, n):
                self.chessboard[row][col] = 'Q'
                self.backtracking(n, row + 1)
                self.chessboard[row][col] = '.'

    def isValid(self, row, col, n):
        # 因为我们在N 皇后回溯搜索的过程中，是按行从上往下一个一个放皇后的，所以不需要检查行方向冲突

        # 检查列方向是否有皇后冲突
        for i in range(row):
            if self.chessboard[i][col] == 'Q':
                return False

        # 检查左上角 ↖ 对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 检查右上角 ↗ 对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True


if __name__ == "__main__":
    solution = Solution()
    n = 4
    res = solution.solveNQueens(n)
    print(res)
