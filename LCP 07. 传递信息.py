from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        pre = set()
        pre.add(0)
        cur = set()
        pre_result = [0] * n
        pre_result[0] = 1
        cur_result = [0] * n
        for i in range(k):
            for r in relation:
                if r[0] in pre:
                    cur_result[r[1]] += pre_result[r[0]]
                    cur.add(r[1])
            pre_result = cur_result.copy()
            cur_result = [0] * n
            pre = cur.copy()
            cur = set()            
        return pre_result[-1]

s = Solution()
print(s.numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3))
        