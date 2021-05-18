class Node:
  def __init__(self, data: int):
    self.left = None
    self.right = None
    self.data = data

  def left_insert(self, data: int):
    if self.left == None:
      self.left = Node(data)
    else:
      self.left.insert(data)
  
  def right_insert(self, data: int):
    if self.right == None:
      self.right = Node(data)
    else:
      self.right.insert(data)

  def insert(self, data: int):
    if self.data > data:
      self.left_insert(data)
    else:
      self.right_insert(data)
  
  def print_pre_order_traversal(self):
    print(self.data, end=' ')
    if self.left:
      self.left.print_pre_order_traversal()
    if self.right:
      self.right.print_pre_order_traversal()

  def print_in_order_traversal(self):
    if self.left:
      self.left.print_in_order_traversal()
    print(self.data, end=' ')
    if self.right:
      self.right.print_in_order_traversal()

  def print_post_order_traversal(self):
    if self.left:
      self.left.print_post_order_traversal()
    if self.right:
      self.right.print_post_order_traversal()
    print(self.data, end=' ')


tree = Node(2)
tree.insert(5)
tree.insert(3)
tree.insert(1)
print("Pre Order Traversal")
tree.print_pre_order_traversal()
print("\nIn Order Traversal")
tree.print_in_order_traversal()
print("\nPost Order Traversal")
tree.print_post_order_traversal()


        
