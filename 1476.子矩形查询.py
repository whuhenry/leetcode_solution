#
# @lc app=leetcode.cn id=1476 lang=python3
#
# [1476] 子矩形查询
#

from typing import List

# @lc code=start
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.update = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append([row1, col1, row2, col2, newValue])


    def getValue(self, row: int, col: int) -> int:
        for rect in self.update[::-1]:
            if row >= rect[0] and row <= rect[2] and col >= rect[1] and col <= rect[3]:
                return rect[4]
        return self.rectangle[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end

