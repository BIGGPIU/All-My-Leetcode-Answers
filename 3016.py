Sample = "xyzxyzxyzxyz"
numpad = {
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
    9:[],
}

charindexes = {

}
from collections import Counter
class Solution:
    # def minimumPushes(self, n: str) -> int:
    #     i = 2
    #     x = 0
    #     answer = 0
    #     while x != len(n):
    #         if i == 10:
    #             i = 2
    #         if n[x] not in charindexes.keys():
    #             numpad[i].append(n[x])
    #             charindexes.update({n[x]:(numpad[i].index(n[x]))+1}) #this uses 1 based indexing
    #             i += 1
    #         x += 1
        
    #     c = dict(Counter(n))

    #     for key in c.keys():
    #         answer += charindexes[key]*c[key]

    #     return answer
    
    def minimumPushes(self, n: str) -> int:
        i = 2
        x = 0
        answer = 0
        c = dict(Counter(n))
        z = dict(sorted(c.items(),key=lambda item: item[1],reverse=True))

        for a in z.keys():
            if i == 10:
                i =2
            if a not in charindexes.keys():
                numpad[i].append(a)
                charindexes.update({a:(numpad[i].index(a))+1})
                i+=1 

        for key in c.keys():
            answer += charindexes[key]*c[key]

        return answer


if __name__ == "__main__":
    hold = Solution.minimumPushes(None,Sample)
    print (hold)