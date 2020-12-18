#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

from typing import List

# @lc code=start
class Solution:
    def fill(self, row, col):
        self.board[row][col] = 'I'
        for dir in self.dirs:
            new_r = row + dir[0]
            new_c = col + dir[1]
            if 0 <= new_r < self.m and 0 <= new_c < self.n:
                if self.board[new_r][new_c] == 'O':
                    self.fill(new_r, new_c)
        pass

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.board = board
        self.m = len(board)
        if 0 == self.m:
            return
        self.n = len(board[0])
        for j in range(self.n):
            if board[0][j] == 'O':
                self.fill(0, j)
            if board[self.m - 1][j] == 'O':
                self.fill(self.m - 1, j)
        for i in range(self.m):
            if board[i][0] == 'O':
                self.fill(i, 0)
            if board[i][self.n - 1] == 'O':
                self.fill(i, self.n - 1)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'I':
                    board[i][j] = 'O'
            
# @lc code=end

