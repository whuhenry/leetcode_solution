#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        while head < tail:
            center = (head + tail) // 2
            if isBadVersion(center):
                tail = center
            else:
                head = center + 1
        return head
        
# @lc code=end

