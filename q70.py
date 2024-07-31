Sample = ""
Sample2 = ""
Sample3 = ""
class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0
        if n < 3:
            return n
        #this can only be reached if the number is above 4
        if (n % 2) == 0: #for each four numbers, how many solutions can you derive from it?
            if (n % 4) == 0:
                for i in range(n//4): # 1+1+1+1,1+1+2,2+2,1+2+1,2+1+1
                    answer+=5
            else:
                for i in range(n//2): #1+1,2
                    answer+=2
        else: 
          if (n % 5) == 0: #for every 5 numbers, how many solutions can you derive from it?
              for i in range(n//5):
                  answer+=8
          else: #for every 3 numbers, how many solutions can you derive from it?
              for i in range(n//3):
                  answer+=3
        return answer



if __name__ == "__main__":
    hold = Solution.climbStairs(None,Sample)
    print (hold)