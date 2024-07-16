Sample = [1,0,1,1]
Sample2 = 1
class Solution:
    def question(self,nums:list,k:int):
        mem = {}
        for i in nums:
            if i in mem.keys():
                mem[i] += 1
            else:
                mem[i] = 1
            
            if 2 in list(mem.values()):
                sorted(mem)
                get = list(mem.keys())[0]
                break
        val1 = nums.index(get)
        nums.remove(get)
        val2 = nums.index(get)+1
        if abs(val1 - val2) <= k:
            return True
        return False 



if __name__ == '__main__':
    hold = (Solution.question(None,Sample,Sample2))
    print (hold)