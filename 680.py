Sample="eedede"
from random import randint
class Solution:
    def validPalindrome(self, s: str) -> bool:
        bitch = 0
        for i in range(len(s)):
            if s[i] == s[-i-1]:
                pass
            else:
                bitch+=1

        if bitch >= 4 and len(s) > 3:
            return False
        if bitch >= 1 and 3 >= len(s):
            return False
        else: 
            return True

if __name__ == "__main__":
    hold = Solution.validPalindrome(None,Sample)
    print (hold)