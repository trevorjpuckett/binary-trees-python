# ##########################################################################
# PROMPT:
# for a given binary tree:
#        [1]
#      /     \
#    [2]     [3]
#   /   \    /  \
# [4]   [5][6]  [7]
# 
# 1) return the tree printed InOrder
#     the outcome should be 4 2 5 1 6 3 7
# 
# 2)  return the tree height including the trunk
#       the outcome should be 3
#
# 2)  return the tree height not including the trunk
#       the outcome should be 2
# ##########################################################################


from src.Tree import Factory as TreeFactory

def main():
    tree = TreeFactory.CreateSample()
    print('Tree in order:')
    tree.traverse.inOrder(tree.trunk)
    print()

    print('Tree height (including trunk):')
    print(tree.height(tree.trunk, includeTrunk=True))

    print('Tree height (not including trunk):')
    print(tree.height(tree.trunk, includeTrunk=False))

if __name__ == '__main__':
    main()