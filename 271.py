sample = ["neet","code","love","you"]

class Solution:

    def encode(self, strs: list[str]) -> str:
        encrypted = []

        for string in strs:
            string = string.replace(".","#")
            string = string.replace(",","^")
            string = string.replace("a",",.....|") #there are 6 dots in this line 
            string = string.replace("b",".,....|")
            string = string.replace("c","..,...|")
            string = string.replace("d","...,..|")
            string = string.replace("e","....,.|")
            string = string.replace("f",".....,|")
            string = string.replace("g",",,....|")
            string = string.replace("h",",.,...|")
            string = string.replace("i",",..,..|")
            string = string.replace("j",",...,.|")
            string = string.replace("k",",....,|")
            string = string.replace("l",",,,...|")
            string = string.replace("m",",,.,..|")
            string = string.replace("n",",,..,.|")
            string = string.replace("o",",,...,|")
            string = string.replace("p",",,,,..|")
            string = string.replace("q",",,,.,.|")
            string = string.replace("r",",,,..,|")
            string = string.replace("s",",,,,,.|")
            string = string.replace("t",",,,,.,|")
            string = string.replace("u",",,,,,,|")
            string = string.replace("v","....,,|")
            string = string.replace("w","...,.,|")
            string = string.replace("x","..,..,|")
            string = string.replace("y",".,...,|")
            string = string.replace("z","...,,,|")
            string = string.replace(" ","_")
            string = string.replace("A",",*****|") 
            string = string.replace("B","*,****|")
            string = string.replace("C","**,***|")
            string = string.replace("D","***,**|")
            string = string.replace("E","****,*|")
            string = string.replace("F","*****,|")
            string = string.replace("G",",,****|")
            string = string.replace("H",",*,***|")
            string = string.replace("I",",**,**|")
            string = string.replace("J",",***,*|")
            string = string.replace("K",",****,|")
            string = string.replace("L",",,,***|")
            string = string.replace("M",",,*,**|")
            string = string.replace("N",",,**,*|")
            string = string.replace("O",",,***,|")
            string = string.replace("P",",,,,**|")
            string = string.replace("Q",",,,*,*|")
            string = string.replace("R",",,,**,|")
            string = string.replace("S",",,,,,*|")
            string = string.replace("T",",,,,*,|")
            string = string.replace("U",",,,,,,|")
            string = string.replace("V","****,,|")
            string = string.replace("W","***,*,|")
            string = string.replace("X","**,**,|")
            string = string.replace("Y","*,***,|")
            string = string.replace("Z","***,,,|")
            encrypted.append(string)
        return encrypted

    def decode(self, s: str) -> list[str]:
        string = str(s)
        string = string.replace('"[',"")
        string = string.replace(']"',"")
        string = string.replace("#",".")
        string = string.replace("^",",")
        string = string.replace(",.....|","a") #there are 6 dots in this line 
        string = string.replace(".,....|","b")
        string = string.replace("..,...|","c")
        string = string.replace("...,..|","d")
        string = string.replace("....,.|","e")
        string = string.replace(".....,|","f")
        string = string.replace(",,....|","g")
        string = string.replace(",.,...|","h")
        string = string.replace(",..,..|","i")
        string = string.replace(",...,.|","j")
        string = string.replace(",....,|","k")
        string = string.replace(",,,...|","l")
        string = string.replace(",,.,..|","m")
        string = string.replace(",,..,.|","n")
        string = string.replace(",,...,|","o")
        string = string.replace(",,,,..|","p")
        string = string.replace(",,,.,.|","q")
        string = string.replace(",,,..,|","r")
        string = string.replace(",,,,,.|","s")
        string = string.replace(",,,,.,|","t")
        string = string.replace(",,,,,,|","u")
        string = string.replace("....,,|","v")
        string = string.replace("...,.,|","w")
        string = string.replace("..,..,|","x")
        string = string.replace(".,...,|","y")
        string = string.replace("...,,,|","z")
        string = string.replace(",*****|","A") 
        string = string.replace("*,****|","B")
        string = string.replace("**,***|","C")
        string = string.replace("***,**|","D")
        string = string.replace("****,*|","E")
        string = string.replace("*****,|","F")
        string = string.replace(",,****|","G")
        string = string.replace(",*,***|","H")
        string = string.replace(",**,**|","I")
        string = string.replace(",***,*|","J")
        string = string.replace(",****,|","K")
        string = string.replace(",,,***|","L")
        string = string.replace(",,*,**|","M")
        string = string.replace(",,**,*|","N")
        string = string.replace(",,***,|","O")
        string = string.replace(",,,,**|","P")
        string = string.replace(",,,*,*|","Q")
        string = string.replace(",,,**,|","R")
        string = string.replace(",,,,,*|","S")
        string = string.replace(",,,,*,|","T")
        string = string.replace(",,,,,,|","U")
        string = string.replace("****,,|","V")
        string = string.replace("***,*,|","W")
        string = string.replace("**,**,|","X")
        string = string.replace("*,***,|","Y")
        string = string.replace("***,,,|","Z")
        string = string.replace("_"," ")
        string.split(",")
        return string


if __name__ == "__main__":
    hold = Solution.encode(None,sample)
    print (Solution.decode(None,hold))