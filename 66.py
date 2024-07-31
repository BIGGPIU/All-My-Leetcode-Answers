Sample = [1,2,3]
Sample2 = ""
Sample3 = ""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        hold = "".join(str(e) for e in digits)
        hold = str(int(hold)+1)
        answer = []
        for i in hold:
            answer.append(int(i))
        return answer


if __name__ == "__main__":
    hold = Solution.plusOne(None,Sample)
    print (hold)