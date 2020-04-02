from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count_live = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        ii = i + di
                        jj = j + dj
                        if ii < 0 or ii >= m or jj < 0 or jj >= n:
                            continue
                        if board[ii][jj] == 1 or board[ii][jj] == 2:
                            count_live += 1
                
                if board[i][j] == 1:
                    if count_live < 2 or count_live > 3:
                        board[i][j] = 2
                elif board[i][j] == 0:
                    if count_live == 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] ==3:
                    board[i][j] = 1
        
                    
s = Solution()
s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
                