# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        new = []
        while current :
            new.append(current.val)
            current = current.next
        val = ""
        for i in new:
            val+=str(i)
        return int(val, 2)       
