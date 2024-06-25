Sample = [1,2,3,4,5,6,7,1,2,3,6,3,3,3]
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counted = Counter(nums)
        answerlist = []
        hold = counted.most_common(k)
        for i in range(k):
            answerlist.append(hold[i][0])
        return answerlist



if __name__ == "__main__":
    print (Solution.topKFrequent(None,Sample,2))