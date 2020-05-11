# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeNthFromEnd(head, n):
    """ Time Complexity: O(n) it depends on the number of Nodes!
    head: ListNode
    n: int
    output: ListNode
    """
    node = head
    size = 0
    # Loop through to count nodes
    while node is not None:
        size += 1
        node = node.next
    node = head
    # If deleting the only node in the list
    if size == 1:
        return None
    # if deleting the head
    elif size == n:
        return head.next
    # else, find the node and delete it
    for _ in range(size-n-1):
        node = node.next
    node.next = node.next.next
    # return the head
    return head

