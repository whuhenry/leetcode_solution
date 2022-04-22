#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

from typing import List

# @lc code=start

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f_cur = 0
        
        for i, num in enumerate(nums, 0):
            f_cur += i * num
        f_max = f_cur

        nums_sum = sum(nums)
        ptr = len(nums) - 1

        for i in range(1, len(nums)):
            f_cur += nums_sum
            f_cur -= nums[ptr] * len(nums)
            ptr -= 1
            # print(f_cur)
            f_max = max(f_max, f_cur)
        return f_max
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxRotateFunction([4, 3, 2, 6]))
