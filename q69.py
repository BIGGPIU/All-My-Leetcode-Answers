Sample = 8
import math
class Solution:
    def question(self,x):
        L,R = 1,x # set two variables to one and the given

        while L <= R: 
            m = (L+R) // 2 #this gets the midpoint of L and R (for averages its x+y/2, doubling the slashes just makes sure its an interger)
            MS = m*m #this gets the value of the midpoint squared

            if MS == x: # if the midpoint squared is x then its the answer
                return m
            elif MS < x: #if midpoint less than x then L increases
                L = m + 1
            else: #if midpoint greater than x than midpoint then R decreases
                R = m - 1
        return R #otherwise just return R
            
                
# as an example for a square root like 8 it would create a tree that would look something like this
# Desired answer: 11
#                  142
#                /      \
#              1 - 71.5  142    
#              |
#              2 - 
#               so on and so forth
#               
#
#
#
#
#

if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)