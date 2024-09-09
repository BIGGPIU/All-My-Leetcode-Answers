Sample = [-4,-2,1,4,8]
class Solution:
    def question(self,nums:list) -> int: 
        nums.sort()
        mem = 9999
        for i in nums:
            print (abs(i))
            if abs(i) <= abs(mem):
                mem = i
        return mem



if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)