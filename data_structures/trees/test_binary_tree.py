from binary_tree import MyBinaryTree, MyBinaryTreeNode

root = MyBinaryTreeNode('name_0')
node1 = MyBinaryTreeNode('name_1')
node2 = MyBinaryTreeNode('name_2')
node3 = MyBinaryTreeNode('name_3')
node4 = MyBinaryTreeNode('name_4')
node5 = MyBinaryTreeNode('name_5')
node6 = MyBinaryTreeNode('name_6')
node7 = MyBinaryTreeNode('name_7')
node8 = MyBinaryTreeNode('name_8')
node9 = MyBinaryTreeNode('name_9')
node10 = MyBinaryTreeNode('name_10')
node11 = MyBinaryTreeNode('name_11')
node12 = MyBinaryTreeNode('name_12')


tree = MyBinaryTree()
tree.add(tree.root, root, 'left')
tree.add(tree.root, node1, 'left')
tree.add(node1, node2, 'left')
tree.add(node2, node3, 'left')

tree.add(tree.root, node4, 'right')
tree.add(node4, node5, 'left')
tree.add(node4, node6, 'right')

tree.add(node6, node7, 'left')
tree.add(node7, node8, 'right')

tree.add(node5, node9, 'right')
tree.add(node9,node10, 'right')

tree.add(node1, node11, 'right')
tree.add(node2, node12, 'right')

tree.print_tree(tree.root)