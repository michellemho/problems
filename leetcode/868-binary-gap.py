class Solution:
    def binaryGap(self, n: int) -> int:
        binary = []
        b = bin(n).replace('0b','')
        curr_max = 0
        counter = 0
        another_one = False
        for n, i in enumerate(b):
            if i == '0':
                counter += 1
            elif i == '1' and n != 0: # 1 is found (not at start)
                another_one = True
                counter += 1
                if counter > curr_max:
                    curr_max = counter
                counter = 0
            # print(counter, curr_max)
        if not another_one: # only one 1 found (at the beginning)
            return 0
        else:
            return curr_max
