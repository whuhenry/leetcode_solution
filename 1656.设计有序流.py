#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
import collections

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.stream = collections.OrderedDict()


    def insert(self, id: int, value: str) -> List[str]:
        if id < self.ptr:
            return []
        elif id > self.ptr:
            self.stream[id] = value
            return []
        else:
            result = [value]
            for i in range(id + 1, self.n + 1):
                if i not in self.stream:
                    self.ptr = i
                    break
                else:
                    result.append(self.stream[i])
                    del self.stream[i]
            return result



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
# @lc code=end

