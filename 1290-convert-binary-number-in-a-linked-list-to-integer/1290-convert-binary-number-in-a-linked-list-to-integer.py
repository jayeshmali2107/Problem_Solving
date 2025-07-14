class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans, curr=0, head
        while curr:
            ans=(ans<<1)+curr.val
            curr=curr.next
        return ans