Sample = [10,4,8,3]
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        leftsumlist = []
        rightsumlist = []
        answer = []
        for i in range(len(nums)):
            x = 1
            rightsum = 0
            leftsum = 0
            if i == 0:
                pass
            else:
                while True:
                    if i-x > -1:
                        leftsumlist.append(nums[i-x])
                        x+=1
                    else:
                        break
                    

            x = 1

            if i == len(nums):
                pass
            else:
                while True:
                    if i+x < len(nums):
                        rightsumlist.append(nums[i+x])
                        x+=1
                    else:
                        break
            
            x = 1

            for z in leftsumlist:
                leftsum += z
            for z in rightsumlist:
                rightsum += z

            appendme = abs(leftsum - rightsum)
            answer.append(appendme)
            rightsumlist = []
            leftsumlist = []
        return answer

if __name__ == "__main__":
    hold = Solution.leftRightDifference(None,Sample)
    print (hold)