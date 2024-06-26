Sample = [-1,1,0,-3,3]
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i = 0 
        ii = 0
        newthing = 1
        newlist = []
        while i != len(nums):
            if 0 >= nums[i]:
                newlist.append(0)
                i+=1
            else:
                while ii != len(nums):
                    if i == ii:
                        hold = newthing*1
                    elif nums[ii] == 0:
                        hold = newthing*1
                    else:
                        hold = newthing*nums[ii]
                    newthing = hold
                    
                    ii+=1
                if 0 >= newthing:
                    newlist.append(0)
                else:
                    newlist.append(newthing)
                newthing = 1
                i+=1
                ii = 0
        return newlist
                    


#unsubmitted

if __name__ == '__main__':
    hold = (Solution.productExceptSelf(None,Sample))
    print (hold)