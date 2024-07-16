Sample = [8,4,4]
from collections import Counter
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        c = dict(Counter(nums))
        hold = list(c.values())
        nums.sort()
        hold.sort(reverse=True)

        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if hold[0] == 3:
            return "equilateral"
        elif hold[0] == 2:
            return "isosceles"
        elif hold[0] == 1:
            return "scalene"

if __name__ == "__main__":
    hold = Solution.triangleType(None,Sample)
    print (hold)