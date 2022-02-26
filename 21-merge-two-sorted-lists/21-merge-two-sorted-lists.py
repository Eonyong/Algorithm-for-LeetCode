# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = _next = ListNode()
        
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    _next.next = ListNode(list1.val)
                    _next = _next.next
                    list1 = list1.next
                else:
                    _next.next = ListNode(list2.val)
                    _next = _next.next
                    list2 = list2.next
            
            elif list1:
                _next.next = ListNode(list1.val)
                _next = _next.next
                list1 = list1.next
                
            elif list2:
                _next.next = ListNode(list2.val)
                _next = _next.next
                list2 = list2.next
        else:
            return answer.next
        