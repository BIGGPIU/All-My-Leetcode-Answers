#You are given a binary array nums and an integer k.

#A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

#Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

#A subarray is a contiguous part of an array.
nums = [0,0,0,1,0,1,1,0]
k = 3
from collections import Counter
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        counting = Counter(nums)
        count = dict(counting)
        if (k%2) == 0:
            keven = True
        else:
            keven = False
        if len(nums)%2 == 0:
            numseven = True
        else:
            numseven = False
        x = 0
        i = 0
        onein = False
        zeroin = False
        if len(nums) == k:
            if 1 in nums:
                onein = True
                answer = 0
            if 0 in nums:
                zeroin = True
                answer = 1
            if zeroin and onein == True:
                answer = -1
            return answer
        elif len(count) == 1:
            #if the counter only finds one value
            if keven != numseven and 0 in nums:
                #if k is even and the length of nums is not even 
                answer = -1
                return answer
            elif keven != numseven and 1 in nums:
                answer = 0 
                return answer
            else:   
                answer = (len(nums)/k)
                temp = answer.is_integer()
                if temp == False:
                    #if the last value is not a simple number then its impossible to turn all values of a single repeating number to 1
                    answer = -1
                else:
                    answer = round(answer)
                return answer
        elif k == 1:
            #k=1 is an exception
            answer = count[0]
            return answer
        else:
            pointer = 0
            flops = 0
            while pointer != len(nums)-1:
                i = 0
                dalist = []
                dictsight = {}
                while i != k:
                    dictsight.update({i:nums[pointer+i]})
                    dalist.append(nums[pointer+i])
                    i+=1
                try:
                    dictsight.update({"future":nums[pointer+i]})
                except:
                    dictsight.update({"future":None}) 
                if dictsight["future"] == "0" and dictsight[0] == 0:
                    flops += 1 #for this example now its 100
                    dictsight.clear()
                if dictsight[0] == 0 and dictsight[i-1] == 0 and 1 not in dalist:
                    flops+=1
                if dictsight["future"] == None and 1 not in dictsight.keys():
                    flops+=1
                    return flops
                pointer += 1
            
            if flops == 0:
                return -1
                



            # I deadass just sat here for 10 minutes just pretending to do something I gotta be stupid
            pass
            


        


if __name__ == "__main__":
    print (Solution.minKBitFlips(None,nums,k))

#since this is a hard question ill list some ideas
#check from each instance of 0 if there are k values ahead of it. actually this may just be the solution nvm misread the question
# maybe do the same thing i mentioned above but instead check if k would make a desired sequence