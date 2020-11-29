#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            center = (start + end) // 2
            if guess(center) == 0:
                return center
            elif guess(center) == 1:
                start = center + 1
            else:
                end = center - 1
        return 0
        
# @lc code=end

