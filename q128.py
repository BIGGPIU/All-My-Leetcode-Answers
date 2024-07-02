Sample = [9,1,4,7,3,-1,0,5,8,-1,6]
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        highestdict = {}
        i = 0 
        counter = 1
        pointer = nums[i]
        while True:
            if pointer+1 in nums:
                if pointer == nums[len(nums)-1]:
                    counter+=1
                counter+=1
                pointer+=1
            else:
                if pointer == nums[len(nums)-1]:
                    counter+=1
                try:
                    if sorted(list(highestdict.values()))[0] >= counter:
                        pass
                    else:
                        highestdict.update({i:counter})
                except:
                    highestdict.update({i:counter})
                print (highestdict)
                i+=1
                try:
                    counter = 0
                    pointer = nums[i]
                except:
                    pass
                if i == len(nums)+1:
                    answer = (list(highestdict.values()))
                    answer = sorted(answer)
                    answer = answer[len(answer)-1]
                    return answer

        




if __name__ == '__main__':
    hold = (Solution.longestConsecutive(None,Sample))
    print (hold)