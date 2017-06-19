"""
You’re given the pointer to the head nodes of two linked lists. Compare the data
in the nodes of the linked lists to check if they are equal. The lists are equal
only if they have the same number of nodes and corresponding nodes contain the
same data. Either head pointer given may be null meaning that the corresponding
list is empty.

Input Format
You have to complete the int CompareLists(Node* headA, Node* headB) method which
takes two arguments - the heads of the two linked lists to compare. You should
NOT read any input from stdin/console.

Output Format
Compare the two linked lists and return 1 if the lists are equal. Otherwise,
return 0. Do NOT print anything to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def CompareLists(headA, headB):
    if not headA and not headB:
        return 1
    if (not headA) or (not headB) or (headA.data != headB.data):
        return 0
    return CompareLists(headA.next, headB.next)
