#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

from typing import List

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rest_dict = {}
        comm_dict = {}
        for i, rest in enumerate(list1):
            if rest in rest_dict:
                rest_dict[rest] += i
                comm_dict[rest] = rest_dict[rest]
            else:
                rest_dict[rest] = i
        for i, rest in enumerate(list2):
            if rest in rest_dict:
                rest_dict[rest] += i
                comm_dict[rest] = rest_dict[rest]
            else:
                rest_dict[rest] = i

        sorted_dict = {k: v for k, v in sorted(comm_dict.items(), key=lambda item: item[1])}
        keys = list(sorted_dict.keys())
        result = [keys[0]]
        for i in range(1, len(keys)):
            if sorted_dict[keys[i]] == sorted_dict[keys[0]]:
                result.append(keys[i])
            else:
                break
        return result
# @lc code=end

