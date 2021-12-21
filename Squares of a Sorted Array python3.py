class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        counter = 0
        output = []
        for i in nums:
            output.append(i*i)
        output.sort()
        return output