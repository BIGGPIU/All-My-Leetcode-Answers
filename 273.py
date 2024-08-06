Sample = 123
# one million two hundread thirty four five hundread sixty seven
d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
class Solution:
    def question(self,num:int) -> str:
        pos = 0
        actualnumbers = [1,2,3,4,5,6,7,8,9]
        multis = [100,1000,1000000,1000000000]
        answer = "" 
        testme = []
        appendme = []
        nums = str(num)
        for i in nums:
            if pos == 3:
                testme.append(appendme)
                appendme = []
                appendme.append(i)
                pos = 1
            else:
                appendme.append(i)
                pos += 1 
        testme.append(appendme)
        testme = list(reversed(testme))
        print (testme)
        realans = []
        multifactor = 100
        for i in range(len(testme)):
            testme[i] = list(reversed(testme[i]))
            if len(testme[i]) == 3:
                firsttwo = int(f"{testme[i][0]}{testme[i][1]}")
                answer += f"{d[(int(testme[i][2]))]} "
                answer += f"{d[multis[0]]} "
                try:
                    answer += f"{d[(firsttwo)]} "
                except:
                    answer += f"{d[(int(testme[i][1])*10)]} "
                    answer += f"{d[(int(testme[i][0]))]} "
                
                if i != 0:
                    answer += f"{d[multis[i]]} "
                realans.insert(0,answer)
                answer = ""
            else:
                if len(testme[i])  == 2 :
                    firsttwo = int(f"{testme[i][0]}{testme[i][1]}")
                    answer += d[firsttwo]
                    realans.insert(0,answer)
                else:
                    first = int(f"{testme[i][0]}")
                    answer += f"{d[first]} "
                    answer += f"{d[multis[i]]} "
                    realans.insert(0,answer)
        
        temp = "".join(realans)
        temp = temp[:(len(temp)-1)]

        return temp


if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (Sample)
    print (hold)