Sample = [1,2]
Sample2 = [3,4]
Sample3 = ""
from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return median(sorted(nums1 + nums2))


if __name__ == "__main__":
    hold = Solution.findMedianSortedArrays(None,Sample,Sample2)
    print (hold)