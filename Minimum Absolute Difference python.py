class Solution(object):
    def minimumAbsDifference(self, arr):
        # sort array first
        
        # compare differences between index and index + 1
        
        # first one is smallest
        # if find equal append into list
        # if find smaller clear list and append new smallest
        # if find larger ignore
        
        output = []
        
        arr.sort()
        smallest = arr[1]-arr[0]
        output.append([arr[0],arr[1]])
        for i in xrange(1,len(arr)-1):
            if (arr[i+1]-arr[i] < smallest):
                del (output)
                output = []
                smallest = arr[i+1]-arr[i]
                output.append([arr[i],arr[i+1]])
            elif (arr[i+1]-arr[i] == smallest):
                output.append([arr[i],arr[i+1]])
        return output
        