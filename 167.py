Sample = [0,0,3,4]
Sample2 = 0
Sample3 = ""
#I have an idea for this I want to do tomorrow. create a Counter dictionary and if its value is greater than 2 then its allowed to check itself
from collections import Counter
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        main = 0
        pointer = 1
        allvalues = dict(Counter(numbers))
        allvalueslist = allvalues.keys()
        while True:
            if allvalueslist[main] + allvalueslist[main] == target and allvalues[allvalueslist[main]] >= 2:
                hold = numbers.index(allvalueslist[main])
                numbers[hold] = "x"
                return [hold+1,numbers.index(allvalueslist[main])+1]
            else:
                if allvalueslist[main] + allvalueslist[pointer] == target:
                    return [numbers.index(allvalueslist[main])+1,numbers.index(allvalueslist[pointer])]
                else:
                    pointer += 1
                    if pointer == len(allvalueslist)+1:
                        main+=1
                        pointer = main+1
                
        


if __name__ == "__main__":
    hold = Solution.twoSum(None,Sample,Sample2)
    print (hold)