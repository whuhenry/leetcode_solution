#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

from typing import List

# @lc code=start

import collections

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = list(collections.Counter(nums).items())
        nums_count.sort(key = lambda x : (x[1], -x[0]))
        result = []
        for tmp in nums_count:
            result.extend([tmp[0]] * tmp[1])
        return result


# @lc code=end

s = Solution()
print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1]))