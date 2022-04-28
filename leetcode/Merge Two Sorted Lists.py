from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = [1,2,4]
list2 = [1,3,4]
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list, new_list_head = None, None
        p1, p2 = list1, list2
        while(not(p1 is None and p2 is None)):
            if (p1 is None):
                new_node = ListNode(p2.val)
                if new_list is None:
                    new_list = new_node
                    new_list_head = new_node
                else:
                    new_list.next = new_node
                    new_list = new_list.next
                p2 = p2.next
                continue
            if (p2 is None):
                new_node = ListNode(p1.val)
                if new_list is None:
                    new_list = new_node
                    new_list_head = new_node
                else:
                    new_list.next = new_node
                    new_list = new_list.next
                p1 = p1.next
                continue
            if(p1.val < p2.val):
                new_node = ListNode(p1.val)
                if new_list is None:
                    new_list = new_node
                    new_list_head = new_node
                else:
                    new_list.next = new_node
                    new_list = new_list.next
                p1 = p1.next
            else:
                new_node = ListNode(p2.val)
                if new_list is None:
                    new_list = new_node
                    new_list_head = new_node
                else:
                    new_list.next = new_node
                    new_list = new_list.next
                p2 = p2.next
        return new_list_head




sol = Solution()
print(sol.mergeTwoLists(p1,p2))
