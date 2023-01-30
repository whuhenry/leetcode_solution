#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
from typing import List

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = {}
        for idx, group_size in enumerate(groupSizes, 0):
            if group_size in groups:
                groups[group_size].append(idx)
            else:
                groups[group_size] = [idx]

            if len(groups[group_size]) == group_size:
                    result.append(groups[group_size])
                    groups.pop(group_size)

        return result

# @lc code=end

