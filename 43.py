Sample = "12"
Sample2 = "12"
Sample3 = ""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        for i in range(int(num2)):
            num1 = str(int(num1)+int(num1))
        return num1


if __name__ == "__main__":
    hold = Solution.multiply(None,Sample,Sample2)
    print (hold)