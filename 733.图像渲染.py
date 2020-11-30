#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

from typing import List

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        visited[sr][sc] = True
        nextList = [[sr, sc]]
        steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        src_color = image[sr][sc]
        while len(nextList) > 0:
            new_next_list = []
            for pt in nextList:
                image[pt[0]][pt[1]] = newColor
                for step in steps:
                    nr = pt[0] + step[0]
                    nc = pt[1] + step[1]
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == src_color and not visited[nr][nc]:
                        new_next_list.append([nr, nc])
                        visited[nr][nc] = True
            nextList = new_next_list
        return image
        
# @lc code=end

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

