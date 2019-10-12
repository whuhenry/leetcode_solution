class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isInc = True
        isDec = True
        for i in range(len(A) - 1):
            if isInc and A[i + 1] < A[i]:
                isInc = False
            if isDec and A[i + 1] > A[i]:
                isDec = False
            if (not isInc) and (not isDec):
                return False
        return True
