Sample = "leetcode"
from collections import Counter
class Solution:
    def firstUniqChar(self,s:str):
        c = dict(Counter(s))
        if 1 not in list(c.values()):
            return -1
        for i in list(c.keys()):
            if c[i] == 1:
                return s.index(i)



if __name__ == '__main__':
    hold = (Solution.firstUniqChar(None,Sample))
    print (hold)