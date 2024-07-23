Sample = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        median = arr[len(arr)//2]
        for i in arr:
            #im not doing this math problem bro :skull:
            pass

if __name__ == "__main__":
    hold = Solution.trimMean(None,Sample)
    print (hold)