class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_nums =[0] * len(nums)
        sum_nums[0] = nums[0]
        for i in range(1, len(nums)):
            sum_nums[i] = sum_nums[i - 1] + nums[i]
        result = [0] * len(nums)
        for i in range(n):
            result[i] = nums[i] * (i + 1) - (n - i - 1) * nums[i] - sum_nums[i] + sum_nums[n - 1] - sum_nums[i]
        return result