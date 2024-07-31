Sample = "A man, a plan, a canal: Panama"
Sample2 = ""
Sample3 = ""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        s = re.sub(r'[\W_]+', '', s)
        left = 0
        right = len(s)-1
        while right > left:
            leftget = s[left]
            rightget = s[right]
            if leftget == rightget:
                left+=1
                right+=-1
            else:
                return False
        return True
            




if __name__ == "__main__":
    hold = Solution.isPalindrome(None,Sample)
    print (hold)