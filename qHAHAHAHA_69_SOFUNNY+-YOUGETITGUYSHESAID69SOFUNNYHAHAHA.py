Sample = 9669
class Solution:
    def maximum69Number(self, num: int) -> int:
        newlist = []
        swap = {
            "6":"9",
            "9":"6"
        }
        maxx = num
        num = str(num)
        for i in num:
            newlist.append(i)
        
        for i in range(len(newlist)):
            newlist[i] = swap[newlist[i]]
            x = "".join(newlist)
            x = int(x)
            if x > maxx:
                maxx = x
            newlist[i] = swap[newlist[i]]
        return maxx
    




if __name__ == '__main__':
    hold = (Solution.maximum69Number(None,Sample))
    print (hold)