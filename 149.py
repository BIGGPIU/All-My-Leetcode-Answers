Sample = [[1,1],[2,2],[3,3]]
Sample2 = ""
Sample3 = ""
#this is an algebra problem, each point my conform to y=mx+b
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        points.sort()
        print (points)


if __name__ == "__main__":
    hold = Solution.maxPoints(None,Sample)
    print (hold)