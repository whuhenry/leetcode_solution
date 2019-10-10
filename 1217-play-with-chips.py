class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        for chip in chips:
            if chip % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        return min(oddCount, evenCount)