Sample = [9,1,4,7,3,-1,0,5,8,-1,6]
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        x = 1
        longest = 0
        for i in nums:
            if i - 1 not in nums:
                while True:
                    if i + x in nums:
                        x+=1
                    else:
                        break
                longest=max(x,longest)
                x=1
        return longest
            


if __name__ == "__main__":
    hold = Solution.longestConsecutive(None,Sample)
    print (hold)