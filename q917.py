sample = "dc-ba"
#à
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        converted = []
        allnums = []
        answer = []
        for i in s:
            if i.isalpha() == True:
                converted.append("à")
                allnums.append(i)
            else:
                converted.append(i)
        converted = "".join(converted)
        print (allnums)
        allnums.reverse()

        for i in converted:
            if i == "à":
                hold = allnums.pop(0)
                answer.append(hold)
            else:
                answer.append(i)
        return "".join(answer)
            
            





if __name__ == "__main__":
    hold = Solution.reverseOnlyLetters(None,sample)
    print (hold)