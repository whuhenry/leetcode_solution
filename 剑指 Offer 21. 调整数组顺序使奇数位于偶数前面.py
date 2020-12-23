from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd, even = n - 1, 0
        
        while odd > even:
            if nums[odd] % 2 == 1 and nums[even] % 2 == 0:
                nums[odd], nums[even] = nums[even], nums[odd]
            if nums[odd] % 2 == 0:
                odd -= 1
            if nums[even] % 2 == 1:
                even += 1
        return nums
            
