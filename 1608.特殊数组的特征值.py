#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

from typing import List

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        left_count = len(nums)
        pre_val = None
        keys = list(num_dict.keys())
        keys.sort()
        for k in keys:
            v = num_dict[k]
            if k >= left_count:
                if pre_val is None:
                    return left_count
                elif pre_val < left_count:
                    return left_count
            left_count -= v
            pre_val = k
        return -1

# @lc code=end

s = Solution()
print(s.specialArray([3,6,7,7,0]))