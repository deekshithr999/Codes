
'''
https://leetcode.com/problems/min-stack/description/
'''



class MinStack:

    def __init__(self):
        self.st = []
        self.mini = 0
    def push(self, val: int) -> None:
        if not self.st:
            self.mini = val
            self.st.append(val)
        elif val < self.mini:
            to_app = 2*val - self.mini
            self.st.append(to_app)
            self.mini = val
        elif val >= self.mini:
            self.st.append(val)

    def pop(self) -> None:
        if self.st[-1] < self.mini:
            self.mini = 2*self.mini - self.st[-1]
        self.st.pop()

    def top(self) -> int:
        if self.st[-1]<self.mini:
            return self.mini
        else:
            return self.st[-1]
        
    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:
    '''
    TC: O(n)
    SC: O(2n)
    '''
    def __init__(self):
        self.st = list()
        self.min_st = list()
    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min_st)==0:
            self.min_st.append(val)
        else:
            self.min_st.append(min(self.min_st[-1], val))
    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()
    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int:
        return self.min_st[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()