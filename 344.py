Sample = ["h","e","l","l","o"]
Sample2 = ""
Sample3 = ""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left != right and right > left:
            leftget = s[left]
            rightget = s[right]
            s[left] = rightget
            s[right] = leftget
            left += 1
            right += -1



if __name__ == "__main__":
    hold = Solution.reverseString(None,Sample)
    print (hold)