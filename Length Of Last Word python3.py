class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        found = False
        for i in s[::-1]:
            if i != " ":
                count+=1
                found = True
            elif found:
                break;
        return count