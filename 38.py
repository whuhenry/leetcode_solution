class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        if n == 1:
            return result
        for i in range(1, n):
            tmp = ''
            prechar = None
            count = 0
            for idx, ch in enumerate(result):
                if prechar is None:
                    prechar = ch
                if ch != prechar:
                    tmp += str(count) + prechar
                    count = 1
                    prechar = ch
                else:
                    count += 1
            tmp += str(count) + prechar
            result = tmp
        return result