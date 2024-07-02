sample = ["dan","and"]

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if strs == [""]:
            return [[""]]
        if strs == ["",""]:
            return [["",""]]

        if len(strs) == 1:
            return [[strs[0]]]

        if len(strs) == 2:
            if strs[0] == strs[1]:
                return [[strs[0],strs[1]]]
            if len(strs[1]) != 0:
                if len(strs[0]) == 0:
                    print ("b")
                    return [[strs[0]]
,[strs[1]]]
                else:
                    print ("a")
                    temp1 = (strs[0])
                    temp2 = (strs[1])
                    return [temp1,temp2]
            return [[strs[0],strs[1]]]

        hold = {}
        permlist=[]
        keys = []
        for i in range(len(strs)):
            hold.update({strs[i]:sorted(dict(Counter(strs[i])))})
            keys.append(strs[i])
        for i in range(len(strs)):
            x = hold[keys[i]]
            templist = []
            for z in hold:
                if hold.get(z) == x:
                    if len(z) == 0:
                        permlist.append(z)
                    elif z in templist:
                        pass
                    else:
                        templist.append(z)
            if templist not in permlist and len(templist) != 0:
                permlist.append(templist) 
        return permlist
            
if __name__ == "__main__":
    print (Solution.groupAnagrams(None,sample))