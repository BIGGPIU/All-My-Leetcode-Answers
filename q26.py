nums = [1,1,2]
from collections import Counter
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = Counter(nums)
        ans = []
        counted = dict(c)
        hold = str(counted.keys())
        hold = hold.replace("dict_keys([","")
        hold = hold.replace("])","")
        hold = hold.replace(" ","")
        hold = hold.split(",")
        for i in hold:
            ans.append(str(i))
            ans = sorted(ans)
        ans = "".join(ans)
        return int(ans)
    

if __name__ == "__main__":
    print (Solution.removeDuplicates(None,nums))