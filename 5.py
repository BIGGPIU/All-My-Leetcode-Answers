Sample = "cbbd"
class Solution:
    def question(self,s:str):
        i = 0 
        x = 1
        answer = [0,0] #pos,length
        temp = []
        templeft = []
        tempright = []
        while i != len(s):
            temp.append(s[i]);temp.append(s[i+1])
            if temp == list(reversed(temp)):
                if i-x > 0:
                    pass
            else:
                i+=1
            

if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)