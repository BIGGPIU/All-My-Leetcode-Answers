from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        c2 = Counter(t)
        c = dict(c)
        c2 = dict(c2)
        if c == c2:
            return True
        else:
            return False
        

#40ms runtime beats 91.59% 16.97mb of memory beats 51.15%

if __name__ == "__main__":
    print (Solution.isAnagram(None,"anagram","gramana"))