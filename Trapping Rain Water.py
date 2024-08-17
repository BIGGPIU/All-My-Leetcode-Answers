Sample = [0,1,0,2,1,0,1,3,2,1,2,1]
#incomplete
class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = 0
        maxwater = 0
        temp = 0
        closed = False
        while l != len(height) - 1:
            if height[l] >= 1:
                r+=1
                while r != len(height):
                    try:
                        if height[l] > height[r]:
                            temp += height[l] - height[r]
                            r+=1
                        else:
                            closed = True
                            l = r + 0
                            break
                    except:
                        l += 1
                        r = l + 0
                        break
                if closed == True:
                    maxwater += temp
                    temp = 0
                    closed = False

            else:       
                l+=1
                r+=1
        return maxwater


if __name__ == "__main__":
    hold = Solution.trap(None,Sample)
    print (hold)