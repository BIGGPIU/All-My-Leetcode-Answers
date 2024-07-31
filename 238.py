Sample = [4,3,2,1,2]
        #convienence 1s added
class Solution:
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     i = 0 
    #     ii = 0
    #     newthing = 1
    #     newlist = []
    #     while i != len(nums):
    #         if 0 >= nums[i]:
    #             newlist.append(0)
    #             i+=1
    #         else:
    #             while ii != len(nums):
    #                 if i == ii:
    #                     hold = newthing*1
    #                 elif nums[ii] == 0:
    #                     hold = newthing*1
    #                 else:
    #                     hold = newthing*nums[ii]
    #                 newthing = hold
                    
    #                 ii+=1
    #             if 0 >= newthing:
    #                 newlist.append(0)
    #             else:
    #                 newlist.append(newthing)
    #             newthing = 1
    #             i+=1
    #             ii = 0
    #     return newlist
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [] #[1,2,3,4]
        past = 1  #->
        #[12,16,24,48,24]
        for i in range(len(nums)):
            if i != 0:
                answer.append(past)
                past = past*nums[i]
            else:
                answer.append(past) # [1,1,2,6]
                                    # 1,1,2
        answer.reverse()
        past = 1
        for i in range(len(nums)):
            past = past*nums[-i]
            answer[i] = answer[i] * past
        answer.reverse()
        return answer


#unsubmitted

if __name__ == '__main__':
    hold = (Solution.productExceptSelf(None,Sample))
    print (hold)