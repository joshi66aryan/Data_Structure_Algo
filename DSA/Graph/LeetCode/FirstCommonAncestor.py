class Node:
    def __init__(self, value, left = None, right = None):
        self.value, self.left, self.right = value, left, right

def findNodeInTree(target, root):
    if not root:
        return False
    if target == root:
        return True
    return (findNodeInTree(target, root.left) or findNodeInTree(target, root.right))

def findFirstCommonAncestor(n1,n2,root):
    n1_onLeft = findNodeInTree(n1, root.left)
    n2_onLeft = findNodeInTree(n2, root.left)

    if n1_onLeft ^ n2_onLeft:
        return root
    
    if n1_onLeft:
        return findFirstCommonAncestor(n1,n2,root.left)
    else:
        return findFirstCommonAncestor(n1,n2,root.right)
node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
rootnode = Node(55, node44, node77)
x = findFirstCommonAncestor(node88, node33, rootnode)
print(x.value)
