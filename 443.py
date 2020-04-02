from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        store_idx = 0
        ch_idx = 0
        pre_ch = None
        count_ch = 0
        for ch_idx in range(len(chars)):
            if pre_ch is None:
                pre_ch = chars[ch_idx]
            if pre_ch == chars[ch_idx]:
                count_ch += 1
            else:
                if count_ch == 1:
                    chars[store_idx] = pre_ch
                    store_idx += 1
                else:
                    chars[store_idx] = pre_ch
                    store_idx += 1
                    tmp = str(count_ch)
                    for idx, ch in enumerate(tmp):
                        chars[store_idx] = ch
                        store_idx += 1
                    
                
                pre_ch = chars[ch_idx]
                count_ch = 1
            
        if count_ch == 1:
            chars[store_idx] = pre_ch
            store_idx += 1
        else:
            chars[store_idx] = pre_ch
            store_idx += 1
            tmp = str(count_ch)
            for idx, ch in enumerate(tmp):
                chars[store_idx] = ch
                store_idx += 1
        
        return store_idx
                