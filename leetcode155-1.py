class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = []
        self.helper = []


    def push(self, x: int) -> None:
        self.cnt.append(x)
        if not self.helper or self.helper[-1]>=x:
            self.helper.append(x)



    def pop(self) -> None:
        x = self.cnt.pop()
        if x == self.helper[-1]:
            self.helper.pop()


    def top(self) -> int:
        return self.cnt[-1]


    def getMin(self) -> int:
        return self.helper[-1]