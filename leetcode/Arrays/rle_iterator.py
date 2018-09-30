class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.i = 0
        self.pointer = 0


    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.pointer >= len(self.A):
            return -1
        self.i += n
        while self.i > self.A[self.pointer]:
            self.i = self.i - self.A[self.pointer]
            self.pointer += 2
            if self.pointer >= len(self.A):
                return -1
        return self.A[self.pointer + 1]



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
