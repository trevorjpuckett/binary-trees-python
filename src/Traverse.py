

MOVE_RIGHT = 1
FROM_RIGHT = 1
MOVE_LEFT  = -1
FROM_LEFT  = -1

class Traverse():

    # DEFAULTS TO OUTLINE FROM LEFT MOST LEAF
    def outline(self, root, callback, direction=FROM_LEFT):
        if direction == FROM_LEFT:
            self.bottomUpEdge(root, MOVE_LEFT, callback, includeTrunk=True)
            self.topDownEdge(root,MOVE_RIGHT, callback)
        if direction == FROM_RIGHT:
            self.bottomUpEdge(root, MOVE_RIGHT, callback, includeTrunk=True)
            self.topDownEdge(root,MOVE_LEFT, callback)


    def bottomUpEdge(self,root, direction, callback, includeTrunk=False, index = 0):
        if root is None:
            return
        if direction == MOVE_LEFT:
            self.bottomUpEdge(root.left, MOVE_LEFT, callback, includeTrunk, index+1)
        if direction == MOVE_RIGHT:
            self.bottomUpEdge(root.right,MOVE_RIGHT, callback, includeTrunk, index+1)
        if includeTrunk == False and index == 0:
            return
        callback(root)

    def topDownEdge(self, root, direction, callback, includeTrunk=False, index = 0):
        if root is None:
            return
        if direction == MOVE_LEFT:
            if index != 0 or includeTrunk == True:       
                callback(root)
            self.topDownEdge(root.left, MOVE_LEFT,callback, includeTrunk, index+1)
        if direction == MOVE_RIGHT:      
            if index != 0 or includeTrunk == True:     
                callback(root)
            self.topDownEdge(root.right, MOVE_RIGHT,callback, includeTrunk, index+1)

    # access nodes by: left, root, right
    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data,end=" ")
        self.inOrder(root.right)

    # TODO: access nodes by: root, left, right
    def preOrder(self,root, callback):
        if root is None:
            return
        print(root)
        self.preOrder(root.left)
        self.preOrder(root.right)
        pass

    # TODO: access nodes by: left, right, root
    def postOrder(self,root):
        pass

    # TODO: access nodes by: level by level, left to right
    def breadthFirst(self):
        pass


