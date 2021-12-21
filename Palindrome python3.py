class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range (0,trunc(len(str(x)) / 2)):
            if (str(x)[i] != str(x)[len(str(x))-1-i]):
                return False
        return True
        