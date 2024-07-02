Sample = ["a","b","c"]
Sample2 = "aadsfasf absbs bbab cadsfafs"
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        hold = []
        changed = False
        sentence = sentence.split(" ")
        for i in sentence:
            for o in dictionary:
                if o in i[:len(sentence[0])]:
                    hold.append(o)
                    changed = True
            if i[:len(sentence[0])] not in dictionary and changed == False:
                hold.append(i)
        
        answer = " ".join(hold)
        return answer
        

if __name__ == '__main__':
    hold = (Solution.replaceWords(None,Sample,Sample2))
    print (hold)