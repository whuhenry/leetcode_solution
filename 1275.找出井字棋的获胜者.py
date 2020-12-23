#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

from typing import List

# @lc code=start
class Solution:
    def win(self, chess):
        for i in range(3):
            line_sum = sum(chess[i])
            if line_sum == 3 or line_sum == -3:
                return line_sum // 3
        
        for i in range(3):
            line_sum = 0
            for j in range(3):
                line_sum += chess[j][i]
            if line_sum == 3 or line_sum == -3:
                return line_sum // 3
        
        sum_diag = chess[0][0] + chess[1][1] + chess[2][2]
        if sum_diag == 3 or sum_diag == -3:
            return sum_diag // 3
        sum_diag = chess[0][2] + chess[1][1] + chess[2][0]
        if sum_diag == 3 or sum_diag == -3:
            return sum_diag // 3
        return 0
            

    def tictactoe(self, moves: List[List[int]]) -> str:
        chess = [[0 for i in range(3)] for i in range(3)]
        result = {1: 'A', -1: 'B'}
        for i, move in enumerate(moves):
            val = 1 if i % 2 == 0 else -1 
            chess[move[0]][move[1]] = val
            tmp = self.win(chess)
            if tmp != 0:
                return result[tmp]
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'


# @lc code=end

s = Solution()
print(s.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))