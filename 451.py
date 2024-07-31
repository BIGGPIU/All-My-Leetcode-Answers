Sample = "tree"
from collections import Counter
class Solution:
    def question(self,s:str) -> str:
        c = dict(Counter(s))
        c = list(c.items())

        def mysort(l):
            return l[1]
        answer = ""
        c.sort(reverse=True,key=mysort)
        for i in range(len(c)):
            answer+=c[i][0]*c[i][1]
        return answer



if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)