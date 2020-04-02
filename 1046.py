import bisect
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        stones.sort()
        while (len(stones) > 1):
            x = stones.pop()
            y = stones.pop()
            if x != y:
                z = abs(x - y)
                bisect.insort(stones, z)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]


s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))