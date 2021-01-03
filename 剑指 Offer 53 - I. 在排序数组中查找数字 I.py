import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target)
        return end - start