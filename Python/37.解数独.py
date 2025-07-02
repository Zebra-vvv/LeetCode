from typing import List


# 一句话总结：两层for循环遍历整个棋盘每个位置，第三层for循环尝试填入1~9
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtracking(board)

    def backtracking(self, board):

        for i in range(len(board)):
            for j in range(len(board)):

                # 遇到'.'才说明需要处理，遇到数字就跳过
                if board[i][j] != '.':
                    continue

                # 尝试填入 '1' 到 '9'
                for k in map(str, range(1, 10)):
                    if self.isValid(i, j, k, board):
                        board[i][j] = k
                        result = self.backtracking(board)
                        if result:
                            return True
                        board[i][j] = '.'  # 回溯
                return False  # 9个数都不行，返回 False
        return True  # 所有空位都填完了，成功

    def isValid(self, row, col, val, board) -> bool:
        # 判断行是否有重复
        for i in range(9):
            if board[row][i] == val:
                return False

        # 判断列是否有重复
        for j in range(9):
            if board[j][col] == val:
                return False

        # 判断当前 3x3 的小九宫格是否有重复

        startRow = (row // 3) * 3  # 所在九宫格的左上角格子横坐标
        startCol = (col // 3) * 3  # 所在九宫格的左上角格子纵坐标

        # 从左上角格子坐标开始，遍历所在九宫格
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == val:
                    return False

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    solution.solveSudoku(board)
    for row in board:
        print(row)
