Sample = [1,2,3,4,5,6,7,8,9]
Sample2 = 100000
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        counter = 0
        for i in timeSeries:
            for x in range(duration):
                if i + x in timeSeries:
                    counter += 1
                else:
                    counter += duration
                    break
        return counter
        

if __name__ == "__main__":
    hold = Solution.findPoisonedDuration(None,Sample,Sample2)
    print (hold)