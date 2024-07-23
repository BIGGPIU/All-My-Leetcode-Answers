Sample = [1,2,3,4,5,6,6,6,6]
from collections import Counter
class Solution:
    def question(self,nums:list):
        c = (dict(Counter(nums)))
        hold = list(c.values());hold.sort(reverse=True)
        if hold[0] > 1:
            return True
        else:
            return False



if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)