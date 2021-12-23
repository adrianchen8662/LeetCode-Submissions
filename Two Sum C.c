

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i = 0;
    int x = 0;
    *returnSize = 2;
    int* returnarray = malloc(*returnSize*sizeof(int));
    for (i = 0; i < numsSize; i++)
    {
        for (x = i+1; x < numsSize; x++)
        {
            if ((nums[i] + nums[x] == target))
            {
                returnarray[0] = i;
                returnarray[1] = x;
                return returnarray;
            }
        }
    }
    return returnarray;
}