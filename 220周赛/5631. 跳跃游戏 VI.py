from typing import List

import collections
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = [0] * n
        result[0] = nums[0]
        dq = collections.deque()
        dq.append(0)
        for i in range(1, n):
            result[i] = result[dq[0]] + nums[i]

            if dq[0] < i - k + 1:
                dq.popleft()
            while dq and result[i] > result[dq[-1]]:
                dq.pop()
            dq.append(i)           
            
        return result[-1]

s = Solution()
print(s.maxResult([1,-5,-20,4,-1,3,-6,-3],2))