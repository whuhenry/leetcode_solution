#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

from typing import List

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        sorted_nums_dict= sorted(nums_dict.items(),key=lambda x:x[1], reverse=True)
        max_keys = [sorted_nums_dict[0][0]]

        for i in range(1, len(sorted_nums_dict)):
            if sorted_nums_dict[i][1] == sorted_nums_dict[0][1]:
                max_keys.append(sorted_nums_dict[i][0])
            else:
                break
        
        min_len = len(nums)
        for key in max_keys:
            key_count = 0
            start = None
            for i, num in enumerate(nums):
                if num == key:
                    if start is None:
                        start = i
                    key_count += 1
                    if key_count == nums_dict[key]:
                        min_len = min(i - start + 1, min_len)
        return min_len
# @lc code=end

s = Solution()
print(s.findShortestSubArray([1,2,2,3,1,4,2]))
