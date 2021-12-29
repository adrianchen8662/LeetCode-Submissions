int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
        {
            return mid;
        }
        if (arr[mid] > x)
        {
            return binarySearch(arr, l, mid - 1, x);
        }   
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}

int search(int* nums, int numsSize, int target)
{
    return binarySearch(nums,0,numsSize-1,target);
}