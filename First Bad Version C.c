// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    bool badFound = false;
    while (badFound == false)
    {
        if (isBadVersion(n))
        {
            n--;
        }
        else
        {
            badFound = true;
        }
    }
    return n+1;
}