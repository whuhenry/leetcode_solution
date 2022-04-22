class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                break
        if zero_count == 5:
            return True
        
        false_count = 0
        for i in range(num, num + 5):
            if i not in nums:
                false_count += 1
        if false_count != zero_count:
            return False
        return True