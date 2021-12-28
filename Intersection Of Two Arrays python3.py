class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            for x in nums2:
                if i == x and i not in output:
                    output.append(i)
        return output