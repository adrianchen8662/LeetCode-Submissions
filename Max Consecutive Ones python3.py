class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                total = max(total,count)
            else:
                count = 0
        return total