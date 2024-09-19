# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = s2 = ""

        p1 = l1
        p2 = l2

        res = ListNode()
        curr_node = res
        curr_sum = 0
        while p1 or p2 or curr_sum != 0:
            if p1:
                curr_sum += p1.val
                p1 = p1.next
            
            if p2:
                curr_sum += p2.val
                p2 = p2.next

            newNode = ListNode(curr_sum % 10)
            curr_node.next = newNode
            curr_node = newNode
            curr_sum = int(curr_sum / 10)
        
        return res.next