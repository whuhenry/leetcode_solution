class Solution:
    def massage(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 0:
            return 0
        max_hour = [0 for i in range(count)]
        max_hour[0] = nums[0]
        if count == 1:
            return nums[0]
        max_hour[1] = max(nums[0], nums[1])
        if count == 2:
            return max_hour[1]
        for i in range(2, count):
            max_hour[i] = max(max_hour[i - 1], max_hour[i - 2] + nums[i])
        return max_hour[count - 1]