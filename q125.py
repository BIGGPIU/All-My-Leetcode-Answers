Sample = "A man, a plan,_a_canal — Panama!"
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        s = re.sub(r'[\W_]+', '', s)
        if s == s[::-1]:
            return True
        return False


if __name__ == '__main__':
    hold = (Solution.isPalindrome(None,Sample))
    print (hold)