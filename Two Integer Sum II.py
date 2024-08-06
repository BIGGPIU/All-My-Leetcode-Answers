Sample = [-5,-3,0,2,4,6,8]
Sample2 = 5
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        x = 0
        y = 1
        while True:
            hold = numbers[x] + numbers[y]
            if hold == target:
                return [x+1,y+1]
            elif hold > target:
                x+=1
                y=x+1
            else:
                y+=1
                if y == len(numbers):
                    x+=1
                    y=x+1


if __name__ == "__main__":
    hold = Solution.twoSum(None,Sample,Sample2)
    print (hold)