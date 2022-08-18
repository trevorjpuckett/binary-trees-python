from src.Traverse import Traverse
from src.Node import Node

class Tree():

    def __init__(self, trunk):
        self.trunk = trunk
        self.traverse = Traverse()

    def height(self,root, includeTrunk=False):
        if root is None:
            return 0 if includeTrunk else -1
        left = self.height(root.left, includeTrunk)
        right = self.height(root.right, includeTrunk)
        if left > right:
            return left + 1
        return right + 1

class Factory():

    @staticmethod
    def CreateSample():
        trunk = Node(1)
        trunk.left = Node(2)
        trunk.right = Node(3)
        trunk.left.left = Node(4)
        trunk.left.right = Node(5)
        trunk.right.left = Node(6)
        trunk.right.right = Node(7)
        return Tree(trunk)