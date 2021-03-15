class Solution:
    def validOperations(self, n):
        if n % 2 == 0:
            n = n/2
        elif n == 3 or int(n)&3 == 1:
            n = n - 1
        else:
            n = n + 1
        return n
    def integerReplacement(self, n: int) -> int:
        counter = 0
        while n != 1:
            print(n)
            counter += 1
            n = self.validOperations(n)
        return counter
