class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        y = ""
        start = 0
        if x[0] == "-":
            y+=x[0]
            start = 1
        for i in range(len(x)-1,-1+start,-1):
            y+=x[i]
        y = int(y)
        if y > pow(2,31)-1 or y < -pow(2,31):
            return 0
        return int(y)