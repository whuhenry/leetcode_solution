#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

from typing import List

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ch_log, num_log = [], []
        for log in logs:
            log_parts = log.split()
            if log_parts[1].isdigit():
                num_log.append(log)
            else:
                ch_log.append([log_parts[0], ' '.join(log_parts[1:])])
        ch_log.sort(key=lambda x: (x[1], x[0]))
        ch_log = [' '.join(log) for log in ch_log]
        return ch_log + num_log
# @lc code=end

