class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = [0] * (stackSize * 3)
        self.stack_ptr = [0, stackSize, stackSize * 2]
        self.stackSize = stackSize


    def push(self, stackNum: int, value: int) -> None:
        if self.stack_ptr[stackNum] < self.stackSize * (stackNum + 1):
            self.stack[self.stack_ptr[stackNum]] = value
            self.stack_ptr[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.stack_ptr[stackNum] <= self.stackSize * stackNum:
            return -1
        else:
            self.stack_ptr[stackNum] -= 1
            return self.stack[self.stack_ptr[stackNum]]


    def peek(self, stackNum: int) -> int:
        if self.stack_ptr[stackNum] <= self.stackSize * stackNum:
            return -1
        else:
            return self.stack[self.stack_ptr[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.stack_ptr[stackNum] <= self.stackSize * stackNum



# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)