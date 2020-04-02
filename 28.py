class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        n_len = len(needle)
        result = -1
        for h_idx, h_ch in enumerate(haystack):
            if h_idx + n_len > len(haystack):
                break
            flag = True
            for n_idx, n_ch in enumerate(needle):
                h_ch = haystack[h_idx + n_idx]
                if h_ch != n_ch:
                    flag = False
                    break
            if flag:
                return h_idx
                
            
        return result