class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        if not self.stack2:
            self.stack2.append(x)
        else:
            self.stack1.append(x)

    def pop(self) -> int:
        ele = self.stack2.pop()
        if not self.stack2:
            while self.stack1:
                top = self.stack1.pop()
                self.stack2.append(top)
        return ele


    def peek(self) -> int:
        return self.stack2[-1]        

    def empty(self) -> bool:
        if not self.stack2:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()