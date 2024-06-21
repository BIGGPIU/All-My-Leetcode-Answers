nums = [2,1,9,4,4,56,90,3]
target = 8

class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 2:
            return [0,1]
        z = 0 
        for x in nums:
            i = 1
            if nums[i] == x:
                i+=1
            if nums[z] == x:
                i=z+1
            while i != len(nums):
                if x + nums[i] == target:
                    return [z,i]
                else:
                    i+=1
            z+=1

#optimal non cheated answer 
###class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        dic = dict()
#        dic[nums[0]] = 0
#        for i in range(1,len(nums)): 
#            dif = target - nums[i] 
#            if dif in dic:
#                return [dic[dif], i]
#            dic[nums[i]] = i
#        return [-1,-1]

        
if __name__ == "__main__":
    print (Solution.twoSum(None,nums,target))