#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
from typing import List

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k - 1
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        flag = False
        for i in range(len(self.nums)):
            if self.nums[i] < val:
                self.nums.insert(i, val)
                flag = True
                break
        if not flag:
            self.nums.append(val)
        return self.nums[self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

s = KthLargest(3, [4, 5, 8, 2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))

