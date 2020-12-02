#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#

from typing import List

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        maxSubSequence = [0] * k
        start, end = max(0, k - n), min(k, m)

        for i in range(start, end + 1):
            stack1 = self.getMaxSequence(nums1, i)
            stack2 = self.getMaxSequence(nums2, k - i)
            merged_stack = self.merge(stack1, stack2)
            if self.bigger(merged_stack, maxSubSequence):
                maxSubSequence = merged_stack

        return maxSubSequence
        pass


    def getMaxSequence(self, nums: List[int], k):
        stack = [0] * k
        remain = len(nums) - k
        top = -1

        for i, num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1
        return stack
        pass


    def merge(self, stack1, stack2):
        merged = []
        idx1, idx2 = 0, 0
        len1, len2 = len(stack1), len(stack2)
        while idx1 < len1 or idx2 < len2:
            if idx1 >= len1:
                merged.append(stack2[idx2])
                idx2 += 1
            elif idx2 >= len2:
                merged.append(stack1[idx1])
                idx1 += 1
            else:
                if stack1[idx1] > stack2[idx2]:
                    merged.append(stack1[idx1])
                    idx1 += 1
                elif stack1[idx1] < stack2[idx2]:
                    merged.append(stack2[idx2])
                    idx2 += 1
                else:
                    tmp1, tmp2 = idx1, idx2
                    while tmp1 < len1 and tmp2 < len2 and stack1[tmp1] == stack2[tmp2]:
                        tmp1 += 1
                        tmp2 += 1
                    if tmp1 >= len1 or tmp2 >= len2:
                        if len2 - tmp2 > len1 - tmp1:
                            merged.append(stack2[idx2])
                            idx2 += 1
                        else:
                            merged.append(stack1[idx1])
                            idx1 += 1
                    else:
                        if stack1[tmp1] > stack2[tmp2]:
                            merged.append(stack1[idx1])
                            idx1 += 1
                        else:
                            merged.append(stack2[idx2])
                            idx2 += 1

        return merged


    def bigger(self, seq1, seq2):
        idx = 0
        size = len(seq1)
        for i in range(size):
            if seq1[i] < seq2[i]:
                return False
            elif seq1[i] > seq2[i]:
                return True
        
        return False
        
# @lc code=end

s = Solution()
print(s.maxNumber([5,6,8], [6,4,0], 3))