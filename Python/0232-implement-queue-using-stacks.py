class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            cur = self.stack1.pop()
            self.stack2.append(cur)
        final = self.stack2.pop()
        
        while self.stack2:
            cur = self.stack2.pop()
            self.stack1.append(cur)

        return final
        

    def peek(self) -> int:
        while self.stack1:
            cur = self.stack1.pop()
            self.stack2.append(cur)

        final = self.stack2.pop()            
        self.stack1.append(final)
        
        while self.stack2:
            cur = self.stack2.pop()
            self.stack1.append(cur)

        return final
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()