Sample = ""
class Solution:
    def question(self,s:str):
        seen = []
        for i in s:
            if i in seen:
                return i
            else:
                seen.append(i)


if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)