#
# @lc app=leetcode.cn id=2037 lang=python3
#
# [2037] 使每位学生都有座位的最少移动次数
#

from typing import List

# @lc code=start

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        result = 0
        for seat, student in zip(seats, students):
            result += abs(seat - student)
        
        return result
# @lc code=end

