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

if __name__ == "__main__":
    hold = Solution.largeGroupPositions(None,sample)
    print (hold)