import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = collections.Counter(nums).most_common(1)[0]
        return result[0] if result[1] * 2 > len(nums) else -1