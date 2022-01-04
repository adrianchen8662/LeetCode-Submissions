class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            if digits[i] == 9 and carry == 1:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digits[i] + carry
                carry = 0
        if (carry == 1):
            digits.insert(0,1)
        return digits