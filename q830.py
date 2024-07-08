sample = "abbxxxxzzy"

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        past = ""
        startindex = ""
        endindex = ""
        leading = False
        answerdict = []
        logged = []
        for i in range(len(s)):
            pointer = s[i]
            try:
                hold = s[i+1]
            except:
                hold == None
            if hold == pointer:
                leading = True
            else:
                leading = False
            if leading == True:
                logged.append(i)
            pass
        return logged

            

if __name__ == "__main__":
    hold = Solution.largeGroupPositions(None,sample)
    print (hold)