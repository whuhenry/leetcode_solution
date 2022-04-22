class Solution:
    def firstUniqChar(self, s: str) -> str:
        ch_count = [0] * 26
        ch_start = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            ch_count[idx] += 1
            if ch_start[idx] == -1:
                ch_start[idx] = i
        
        result = ' '
        min_start = len(s)
        for i in range(26):
            if ch_count[i] == 1 and ch_start[i] < min_start:
                min_start = ch_start[i]
                result = chr(i + ord('a'))
        return result