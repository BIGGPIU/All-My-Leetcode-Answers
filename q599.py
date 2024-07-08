sample = ["happy","sad","good"]
sample2 = ["sad","happy","good"]

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hold = {}
        for i in list1:
            if i in list2:
                if (list1.index(i)+list2.index(i) in hold.keys()):
                    pass
                else:
                    hold.update({(list1.index(i)+list2.index(i)):[]})
                hold[(list1.index(i)+list2.index(i))].append(i) 

        hold2 = sorted(hold.keys())
        print (hold2)

        return hold[hold2[0]]
        
if __name__ == "__main__":
    hold = Solution.findRestaurant(None,sample,sample2)
    print (hold)