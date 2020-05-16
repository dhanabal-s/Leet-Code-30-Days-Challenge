class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head):
            odd = head
            even = odd.next
            evenHead = even
            while(even and even.next):
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = evenHead
        return head
        
Time Complexity : O(N)
Space Complexity : O(1)


