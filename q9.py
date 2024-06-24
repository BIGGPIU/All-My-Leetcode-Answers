z = 121
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        hold = list(reversed(x))
        if x == "".join(hold):
            return True
        else:
            return False
        
if __name__ == "__main__":
    print (Solution.isPalindrome(None,z))