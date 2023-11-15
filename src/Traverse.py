FROM_LEFT = -1
FROM_RIGHT = 1


class Traverse():


    def outline(self, root, start, last):
        if root is None:
            return

        if last.left is None:

    # def outline(self, root, start):
    #     self.bottomUpEdge(root,start)

    # def bottomUpEdge(self, root, start, current=None):
    #     if root is None:
    #         return
        
    #     if start not in [FROM_LEFT,FROM_RIGHT]:
    #         raise Exception(f'Invalid traversal startection: {start}')

    #     if start == FROM_LEFT:
    #         self.bottomUpEdge(root.right,start, current=FROM_RIGHT)
    #         self.bottomUpEdge(root.left,start, current=FROM_LEFT)
    #     else:
    #         self.bottomUpEdge(root.left,start, current=FROM_LEFT)
    #         self.bottomUpEdge(root.right,start, current=FROM_RIGHT)

    #     if root.left is None and root.right is None:
    #         print(root,end=" ")
            
    #     elif start == FROM_LEFT and current == FROM_LEFT and root.left is None:
    #         print(root, end=" ")
            
    #     elif start == FROM_RIGHT and current == FROM_RIGHT and root.right is None:
    #         print(root, end=" ")


            












# FROM_RIGHT = 1
# FROM_RIGHT = 1
# FROM_LEFT  = -1
# FROM_LEFT  = -1

# class Traverse():

#     # DEFAULTS TO OUTLINE FROM LEFT MOST LEAF
#     def outline(self, root, callback, startection=FROM_LEFT):
#         if startection == FROM_LEFT:
#             self.bottomUpEdge(root, FROM_LEFT, callback, includeTrunk=True)
#             self.topDownEdge(root,FROM_RIGHT, callback)
#         if startection == FROM_RIGHT:
#             self.bottomUpEdge(root, FROM_RIGHT, callback, includeTrunk=True)
#             self.topDownEdge(root,FROM_LEFT, callback)


#     def bottomUpEdge(self, root, startection, callback, includeTrunk=False, index = 0, stick_to=None):
#         if stick_to is None:
#             stick_to = startection
#         if root is None:
#             return
#         if startection == FROM_LEFT or stick_to == FROM_LEFT:
#             if root.left is not None:
#                 self.bottomUpEdge(root.left, FROM_LEFT, callback, includeTrunk, index+1,stick_to=stick_to)
#             if root.right is not None:
#                 self.bottomUpEdge(root.right, FROM_LEFT, callback, includeTrunk, index+1,stick_to=stick_to)
#         if startection == FROM_RIGHT or stick_to == FROM_RIGHT:
#             self.bottomUpEdge(root.right,FROM_RIGHT, callback, includeTrunk, index+1,stick_to=stick_to)
#         if includeTrunk == False and index == 0:
#             return
#         if stick_to == startection or (root.left is None and root.right is None):
#             callback(root)

#     def topDownEdge(self, root, startection, callback, includeTrunk=False, index = 0, stick_to=None):
#         if stick_to is None:
#             stick_to = startection
#         if root is None:
#             return
#         if startection == FROM_LEFT:
#             if index != 0 or includeTrunk == True:       
#                 callback(root)
#             self.topDownEdge(root.left, FROM_LEFT,callback, includeTrunk, index+1, stick_to=stick_to)
#         if startection == FROM_RIGHT:      
#             if index != 0 or includeTrunk == True:     
#                 callback(root)
#             self.topDownEdge(root.right, FROM_RIGHT,callback, includeTrunk, index+1, stick_to=stick_to)

#     # access nodes by: left, root, right
#     def inOrder(self,root):
#         if root is None:
#             return
#         self.inOrder(root.left)
#         print(root.data,end=" ")
#         self.inOrder(root.right)

#     # TODO: access nodes by: root, left, right
#     def preOrder(self,root, callback):
#         if root is None:
#             return
#         print(root)
#         self.preOrder(root.left)
#         self.preOrder(root.right)
#         pass

#     # TODO: access nodes by: left, right, root
#     def postOrder(self,root):
#         pass

#     # TODO: access nodes by: level by level, left to right
#     def breadthFirst(self):
#         pass


