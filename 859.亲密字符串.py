#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        ch_count = [0] * 26
        diff_idx = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_idx.append(i)
                if len(diff_idx) > 2:
                    return False
            else:
                ch_count[ord(A[i]) - ord('a')] += 1
        if len(diff_idx) == 2:
            if A[diff_idx[0]] == B[diff_idx[1]] and A[diff_idx[1]] == B[diff_idx[0]]:
                return True
            else:
                return False
        elif len(diff_idx) == 1:
            return False
        else:
            for val in ch_count:
                if val >= 2:
                    return True
            return False

# @lc code=end

