#
# @lc app=leetcode.cn id=2216 lang=python3
#
# [2216] 美化数组的最少删除数
#

from typing import List

# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        re = []
        pn = 0
        pr = 0
        while pn < len(nums):
            if pr % 2 == 0:
                re.append(nums[pn])
                pr += 1
            else:
                if nums[pn] != re[pr - 1]:
                    re.append(nums[pn])
                    pr += 1

            pn += 1

        result = len(nums) - len(re)
        if len(re) % 2 == 1:
            result += 1
        return result
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.minDeletion([1,1,2,3,5]))
