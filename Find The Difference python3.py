class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for n in s + t:
            result ^= ord(n)
        return chr(result)