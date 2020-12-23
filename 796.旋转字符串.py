#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for i in range(1, len(A)):
            tailB = A[0: len(A) - i]
            headB = A[len(A) - i: ]
            if headB + tailB == B:
                return True
        return False

        
# @lc code=end

