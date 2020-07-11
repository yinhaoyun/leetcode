from typing import List


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        res = head
        cur = head
        to_link_nodes = []
        while True:
            while cur is not None:
                if cur.child is not None:
                    if cur.next is not None:
                        to_link_nodes.append(cur.next)
                        print("to_link_nodes added:", [node.val for node in to_link_nodes])
                    cur.next = cur.child
                    cur.child = None
                    cur.next.prev = cur
                if cur.next is not None:
                    cur = cur.next
                    print("cur = cur.next=", cur.val)
                else:
                    print("cur.next=None, link next, cur=", cur.val)
                    break
            if len(to_link_nodes) == 0:
                break
            next_node = to_link_nodes.pop()
            print("cur->next_node: cur=", cur.val, ", next=", next_node.val)
            cur.next = next_node
            cur.next.prev = cur
            cur = cur.next
        return res


def create_doubly_linked_list(arr: List[int]) -> Node:
    print("create_doubly_linked_list:", arr)
    res = Node(arr[0], None, None, None)
    cur = res
    cur_level_head = cur
    i = 1
    finding_child = False
    while i < len(arr):
        if arr[i] is None:
            if not finding_child:
                finding_child = True
                print("finding_child, i=", i)
            else:
                cur_level_head = cur_level_head.next
                print("cur_level_head->next", cur_level_head.val)
        else:
            if not finding_child:
                next_node = Node(arr[i], cur, None, None)
                cur.next = next_node
                cur = next_node
                print("cur->next", cur.val)
            else:
                finding_child = False
                child = Node(arr[i], None, None, None)
                print("next level, from", cur_level_head.val)
                cur_level_head.child = child
                cur_level_head = child
                cur = child
        i += 1
    return res


head = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
node = create_doubly_linked_list(head)


def print_doubly_linked_list(head: Node) -> None:
    children = [head]
    while len(children) > 0:
        ll = []  # linked list
        head = children.pop()
        while head is not None:
            ll.append(head.val)
            if head.child is not None:
                children.append(head.child)
            head = head.next
        print(ll)


print_doubly_linked_list(node)
s = Solution()
new_node = s.flatten(node)
print_doubly_linked_list(new_node)

