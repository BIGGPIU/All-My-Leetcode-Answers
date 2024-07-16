Sample = "ABFCACDB"
class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" in s:
                s = s.replace("AB","")
            else:
                if "CD" in s:
                    s = s.replace("CD","")
                else:
                    if "CD" and "AB" not in s:
                        break
                    else:
                        pass

        return len(s)

if __name__ == "__main__":
    hold = Solution.minLength(None, Sample)
    print (hold)