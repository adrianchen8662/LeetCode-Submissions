class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for i in xrange (0,trunc(len(str(x)) / 2)):
            if (str(x)[i] != str(x)[len(str(x))-1-i]):
                return False
        return True