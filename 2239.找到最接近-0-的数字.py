#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

from typing import List

# @lc code=start

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_dist = 1000000
        max_val = -1000000

        for num in nums:
            if abs(num) < min_dist:
                min_dist = abs(num)
                max_val = num
            if abs(num) == min_dist:
                if num > max_val:
                    max_val = num
        return max_val



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findClosestNumber([-4,-2,1,4,8]))