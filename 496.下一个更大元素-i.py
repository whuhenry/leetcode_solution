#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        big_nums2 = {}
        for i in range(len(nums2)):
            find = False
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    big_nums2[nums2[i]] = nums2[j]
                    find = True
                    break
            if not find:
                big_nums2[nums2[i]] = -1
        result = [big_nums2[num] for num in nums1]
        return result


# @lc code=end

