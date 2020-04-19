class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for block_count in range(2, len(s) // 2 + 1):
            if len(s) % block_count == 0:
                len_per_block = len(s) // block_count
                flag = True
                for idx in range(0, len_per_block):
                    if not flag:
                        break
                    for block_idx in range(1, block_count):
                        if s[block_idx * len_per_block + idx] != s[idx]:
                            flag = False
                            break
                if flag:
                    return True
        return False
                    