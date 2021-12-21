class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted = []
        counter1 = 0
        counter2 = 0
        while counter1 < len(nums1) and counter2 < len(nums2):
            if (nums1[counter1] <= nums2[counter2]):
                sorted.append(nums1[counter1])
                counter1+=1
            else:
                sorted.append(nums2[counter2])
                counter2+=1
        if counter1 < len(nums1) and not counter2 < len(nums2):
            while counter1 < len(nums1):
                sorted.append(nums1[counter1])
                counter1+=1
        if counter2 < len(nums2) and not counter1 < len(nums1):
            while counter2 < len(nums2):
                sorted.append(nums2[counter2])
                counter2+=1
        
        if (len(sorted) % 2 == 0):
            return (sorted[trunc(len(sorted)/2)-1] + sorted[trunc(len(sorted)/2)]) / 2;
        else:
            return sorted[trunc(len(sorted)/2)]
        