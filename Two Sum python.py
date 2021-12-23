class Solution(object):
    def twoSum(self, nums, target):
        for i in xrange (len(nums)):
            for x in xrange (i+1,len(nums)):
                if (((nums[i]+nums[x]) == target)):
                    return [i,x]
        