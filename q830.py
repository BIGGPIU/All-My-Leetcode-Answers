sample = "abbxxxxzzy"

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        answer = []
        skip = []
        for i in range(len(s)):
            x = 1
            if i not in skip:
                while True:
                    try:
                        if s[i+x] == s[i]:
                            skip.append(i+x)
                            x+=1
                        else:
                            break
                    except:
                        break
                if x >= 3:
                    answer.append([i,i+x-1])
        return answer
    
    def largeGroupPositionsoptimal(self, s: str) -> list[list[int]]:
        lis =[]#empty list to store the index of the repeated elements >= 3
        j = 0 #variable to the starting index. 
        for i in range(len(s)): #run through the loop
            if i == len(s) - 1 or s[i] != s[i+1]: #if i reaches the last character or if s[i] is not equal to s[i+1] enter the if condition
                if i - j + 1 >= 3: # subtract the index value so the that you get the repeated index if it is >= 3 append it to the list
                    lis.append([j,i])
                j = i + 1 #increment j to i + 1 index for every iteration if it entrs the 1st if condition
        return lis    

if __name__ == "__main__":
    hold = Solution.largeGroupPositions(None,sample)
    print (hold)