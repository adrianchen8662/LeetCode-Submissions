class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        previous = 0
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in reversed(s):
            if (values[i] >= previous):
                value += values[i]
            else:
                value -= values[i]
            previous = values[i]
        return value