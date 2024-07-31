Sample = [0]
Sample2 = 0
Sample3 = [1]
Sample4 = 1
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if 1 >= m:
            if 1 >= n:
                nums1 = nums2
            else:
                nums1 = nums1
        else:
            check = m
            nums1.reverse()
            nums2.reverse() #[6,5,2]
            ii = 0
            for i in range(len(nums1)): #0,0,0,3,2,1
                try:
                    if nums2[ii] >= nums1[-check]:
                        nums1[i] = nums2[ii]
                        ii+=1
                    else:
                        nums1[i] = nums1[-check]
                        nums1[-check] = nums1[-check+1]
                except:
                    break
            nums1.reverse()
        print (nums1)



if __name__ == '__main__':
    hold = (Solution.merge(None,Sample,Sample2,Sample3,Sample4))
    print (hold)