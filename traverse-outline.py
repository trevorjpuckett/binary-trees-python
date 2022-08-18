'''
PROMPT:
for a given binary tree:
    ex:

         1
    2        3
4       5 6      7

1) return the tree printed InOrder
    the outcome should be 4 2 5 1 6 3 7

3)  return the outline data of the tree from right to left.
    the outcome of your function should return 4 2 1 3 7

3)  return the outline data of the tree from left to right.
    the outcome of your function should return 4 2 1 3 7
'''

from src.Tree import Factory as TreeFactory
from src.Traverse import FROM_LEFT, FROM_RIGHT

def printNode(node):
    print(node, end=" ")

def main():
    tree = TreeFactory.CreateSample()
    print('Tree in order:')
    tree.traverse.inOrder(tree.trunk)
    print()

    print('Tree outline from bottom right leaf to bottom left leaf:')
    tree.traverse.outline(
        tree.trunk,
        direction=FROM_RIGHT, 
        callback=printNode 
    )
    print()
    print('Tree outline from bottom left leaf to bottom right leaf:')
    tree.traverse.outline(
        tree.trunk,
        direction=FROM_LEFT, 
        callback=printNode 
    )

if __name__ == '__main__':
    main()

