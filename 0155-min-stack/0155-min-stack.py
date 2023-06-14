# class MinStack:
    
#     def __init__(self):
#         self.stack = []
#         self.minStack = []
    
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         val = min(val, self.minStack[-1] if self.minStack else val)
#         self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]


class MinStack:

    def __init__(self):
        self.minval = None
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append([val,self.minval])
        if self.minval is None or self.minval > val:
            self.minval = val

    def pop(self) -> None:
        if self.minval == self.stk[-1][0]:
            self.minval = self.stk[-1][1]
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()