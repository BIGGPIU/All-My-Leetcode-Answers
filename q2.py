# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linkedlist:

    def __init__(self):
        self.head = None

    def insertintolist(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listone = l1
        listtwo = l2
        add1 = []
        while(listone):
            if listone.next == None:
                add1.append(listone.val)
                break
            add1.append(listone.val)
            listone = listone.next

        while(listtwo):
            if listtwo.next == None:
                add1.append(listtwo.val)
                break
            add1.append(listtwo.val)
            listtwo = listtwo.next

        print (add1)
        halfof = round(len(add1)/2)

        equationpart1 = ""

        for i in add1:
            equationpart1+=str(i)
        
        equationone = equationpart1[:halfof]
        equationtwo = equationpart1[-halfof:]
        reversed(equationone)
        reversed(equationtwo)
        print (equationone)
        print (equationtwo)
        e1 = int(equationone)
        e2 = int(equationtwo)
        answer = str(e1+e2)
        answer = answer[::-1]

        hold = linkedlist()
        
        for ch in answer:
            ch = int(ch)
            hold.insertintolist(ch)

        return hold
        

# I give up its been one hour