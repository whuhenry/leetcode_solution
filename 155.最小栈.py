#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minele = None


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minele is None or x < self.minele:
            self.minele = x

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minele:
            if len(self.stack) == 0:
                self.minele = None
            else:
                self.minele = self.stack[0]
                for val in self.stack:
                    if val < self.minele:
                        self.minele = val


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minele



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

