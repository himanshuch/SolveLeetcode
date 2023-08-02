# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        self.carry=0
        def dfs(l1, l2, cur):
            if not l1 and not l2 and self.carry==0:
                return
                
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + self.carry
            val = total%10
            self.carry = total//10
            cur.next = ListNode(val)
            
            dfs(l1.next if l1 else l1, l2.next if l2 else l2, cur.next)

        
        dfs(l1, l2, cur)
        return dummy.next

            
            
            
            


        
        