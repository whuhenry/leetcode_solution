from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        cur_count =0
        for num in nums:
            if not cur:
                cur = num
                cur_count = 1
            elif cur == num:
                cur_count += 1
            else:
                cur_count -= 1
                if cur_count == 0:
                    cur = None
        return cur

s = Solution()
print(s.majorityElement([1,2,3,2,2,2,5,4,2]))