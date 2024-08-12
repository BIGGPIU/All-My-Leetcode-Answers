Sample = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        answer = 0
        while i != len(nums)-1:
            if nums[i] == nums[i+1]: #if it is not unique
                nums[i] = "X"
            i+=1
        
        for i in nums:
            if i != "X":
                answer+=1
            else:
                nums.remove("X")
                nums.append("_")
        print (answer)
        print (type(answer))
        return int(answer)


if __name__ == "__main__":
    hold = Solution.removeDuplicates(None,Sample)
    print (hold)