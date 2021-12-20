class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
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
        for i in range(1,len(arr)-1):
            if (arr[i+1]-arr[i] < smallest):
                smallest = arr[i+1]-arr[i]
                output = [[arr[i],arr[i+1]]]
            elif (arr[i+1]-arr[i] == smallest):
                output.append([arr[i],arr[i+1]])
        return output