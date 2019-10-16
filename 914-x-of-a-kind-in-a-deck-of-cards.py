class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        numCount = [0 for i in range(10000)]
        for num in deck:
            numCount[num] += 1
        for x in range(2, len(deck) + 1):
            if len(deck) % x == 0:
                flag = True
                for j in numCount:
                    if j != 0 and j % x != 0:
                        flag = False
                        break
                if flag:
                    return True
        return False