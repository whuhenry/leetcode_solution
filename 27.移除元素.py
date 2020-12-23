#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while(idx < len(nums)):
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1
        return
# @lc code=end

