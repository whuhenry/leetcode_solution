#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        result = []
        for col in range(n):
            curcol = col
            flag = True
            for row in range(m):
                if (curcol == 0 and grid[row][curcol] == -1) or (curcol == n - 1 and grid[row][curcol] == 1) or (grid[row][curcol + grid[row][curcol]] != grid[row][curcol]):
                    flag = False
                    break
                else:
                    curcol += grid[row][curcol]
            result.append(curcol if flag else -1)
        return result
            

# @lc code=end

