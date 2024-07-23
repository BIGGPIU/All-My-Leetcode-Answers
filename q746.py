Sample = [1,10,1,5,5,3,2,1,1,5,6,1,10,100,1,5,1]
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        def dp(n):  # define function grass is green
            if n < 2: 
                return cost[n] #if you can reach the bottom of the stairs then you should do it 
            return cost[n] + min(dp(n-1), dp(n-2)) #return the number its on and call the function again to get the lowest number below itself 
		
        length = len(cost) 
        return min(dp(length-1), dp(length-2))

    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        cost.append(0) #to be honest I dont really get this one it feels kind of brute forceisn
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])

if __name__ == "__main__":

    hold = Solution.minCostClimbingStairs2(None,Sample)
    print (hold)