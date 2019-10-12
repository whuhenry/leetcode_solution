class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        minNum = A[0]
        maxNum = A[0]
        for a in A:
            if a < minNum:
                minNum = a
            elif a > maxNum:
                maxNum = a
        return max(0, (maxNum - K) - (minNum + K))
