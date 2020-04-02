from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count_deck = len(deck)
        deck.sort()
        for x in range(2, count_deck + 1):
            if count_deck % x == 0:
                flag = True
                for i in range(count_deck // x):
                    base_num = deck[i * x]
                    for j in range(1, x):
                        if base_num != deck[i * x + j]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    return True
        return False

s = Solution()
print(s.hasGroupsSizeX([1,1]))