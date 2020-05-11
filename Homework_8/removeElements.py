# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # Time Complexity: O(n) it depends on the number of Nodes
        """ Remove all elements from a linked list of integers that have value val.
        head: ListNode
        val: int
        output: ListNode
        """
        node = head
        prev = None
        found = False
        while node is not None:
            if node.val == val:
                if node == head:
                    print("HEAD")
                    head = node.next
                    node.next = None
                elif node.next is None:
                    print("TAIL")
                    if prev is not None:
                        prev.next = None
                        return head
                else:
                    print("MID")
                    prev.next = node.next
                    node.next = None
                return self.removeElements(head, val)
            prev = node
            node = node.next
        return head