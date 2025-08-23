# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 =[]
        while list1:
            arr1.append(list1.val)
            list1=list1.next
        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        merged = sorted(arr1+arr2)
        
        new = ListNode()
        curr = new
        for i in merged:
            curr.next = ListNode(i)
            curr = curr.next
        return new.next

