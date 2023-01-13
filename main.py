#a program to compute the height of node u in a binary tree

class BinaryTreeNode:
    # initialize an empty binary tree
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    # define a function to add the child of the tree
    def add_child(self,data):
        if data==self.data:
            return True
        # create a left and a right node to add
        # if the left and right node is empty
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)  # creating new node
                else:
                    self.left.add_child(data)
            if data>self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)  # to create a new node since there is no
                else:
                    self.right.add_child(data)
    # define a function to list elemnts of the tree in order transversal
    def in_order_traversal(self, root):
        elements = [] # empty list to append the data
        # if there is a root
        # it will append the data of the left then the right
        if root:
            elements = self.in_order_traversal(root.left)
            elements.append(root.data)
            elements = elements + self.in_order_traversal(root.right) # add elements of the right after the left
        return elements

    # define a function to count the height of the tree
    def height2(u):
        elements = [] # initialize empty list to append data of u
        height = 0
        # if the tree is empty
        if u is None:
             return 0
        elements.append(u)
        while True:
            # position store nodes at a particular level
            position = len(elements) # assign initial value for position
            if position == 0:  # if there is no element return height
                return height-1 #decrement by 1 since position starts from 0, it position go until length -1
            height += 1  # increase height
            # use a while loop
            # position = length of element, so it will decrease in the loop
            while (position > 0):
                parent = elements[0]
                elements.pop(0)
                # append each data from the left and right in to the list
                if parent.left is not None:
                    elements.append(parent.left) #append left child
                if parent.right is not None:
                    elements.append(parent.right)#append right child
                position=position-1 # decrement the position
# test code by adding data for binary search tree
root = BinaryTreeNode(27)
root.add_child(14)
root.add_child(35)
root.add_child(10)
root.add_child(19)
root.add_child(31)
root.add_child(42)
root.add_child(5)

# print the height of the tree
print(root.in_order_traversal(root))
print(root.height2())
#test code for binary tree
root1=BinaryTreeNode(10)
root1.left=BinaryTreeNode(20)
root1.right=BinaryTreeNode(30)
root1.left.left=BinaryTreeNode(19)
root1.left.right=BinaryTreeNode(34)

print(root1.in_order_traversal(root1))
print(root1.height2())


# the big O is O(n) to find the height of the tree