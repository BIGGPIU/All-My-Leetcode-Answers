Sample = 6
def remove(List:list,max,move,pos):
    i = pos
    newlist = []
    while max > i:
        try:
            newlist.append(List[i])
        except:
            return newlist
        i+=move
    return newlist

class Solution:
    def question(self,n):
        List = []
        for i in range(n):
            List.append(i+1)
        
        while len(List) != 1:
            List = remove(List,len(List),2,0)
            List.reverse()
            List = remove(List,len(List),2,1)
            List.reverse() 
        return List
        



if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)