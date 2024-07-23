Sample = 144
class Solution:
    def question(self,num):
        i = 1
        while True:
            if i * i == num:
                return True
            elif i * i > num:
                return False
            else:
                i+=1



if __name__ == '__main__':
    hold = (Solution.question(None,Sample))
    print (hold)