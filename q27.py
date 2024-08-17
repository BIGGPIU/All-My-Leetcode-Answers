from collections import Counter
Sample = [3,2,2,3]
Sample2 = 3
class Solution:
    def removeElement(self,nums,val:int):
        l = 0
        r = len(nums) - 1

        if nums[r] == val:
            nums[r] = "_"
        while (nums[l] != "_"):
            if nums[l] == val:
                nums[l] = "_"
                nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r += -1

    def check(answer):
        if len(answer) != len(Sample):
            return False
        temp = []
        for i in Sample:
            if i == Sample2:
                temp.append("_")
            else:
                temp.append(i)

        c = dict(Counter(temp))
        c2 = dict(Counter(answer))
        if c != c2:
            return False
        return True

if __name__ == '__main__':
    Solution.removeElement(None,Sample,Sample2)
    print (Solution.check(Sample))