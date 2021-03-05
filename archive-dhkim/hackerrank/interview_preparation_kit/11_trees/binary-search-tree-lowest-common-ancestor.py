
"""
https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    # Enter your code here

    range_start = min(v1, v2)
    range_end = max(v1, v2)

    result_nodes = []

    def traverse(node) -> bool:
        if not node:
            return False

        left = traverse(node.left) if node.info >= range_start else False
        right = traverse(node.right) if node.info <= range_end else False

        if (left and right) or ((left or right) and node.info in [v1, v2]):
            result_nodes.append(node)

        if node.info in [v1, v2]:
            return True

        return left or right

    traverse(root)

    if result_nodes:
        return result_nodes[0]

    return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
