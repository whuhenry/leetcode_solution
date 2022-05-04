#
# @lc app=leetcode.cn id=2215 lang=python3
#
# [2215] 找出两数组的不同
#

from typing import List

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num_set1 = set(nums1)
        num_set2 = set(nums2)
        re1 = num_set1.difference(num_set2)
        re2 = num_set2.difference(num_set1)
        return [list(re1), list(re2)]
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
