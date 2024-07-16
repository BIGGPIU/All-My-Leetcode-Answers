Sample = [1,2,3,4]
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        answer = 0
        for i in range(0,len(nums)+1,1):
            if i == 0:
                x = 1
            else:
                i = x
            if nums[len(nums)] % x == 0:
                answer += nums[i]*nums[i]
        return answer


if __name__ == "__main__":
    hold = Solution.sumOfSquares(None,Sample)
    print (hold)