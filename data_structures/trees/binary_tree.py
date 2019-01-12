"""This module contains my custom classes MyBinaryTree and MyBinaryTreeNode."""


class MyBinaryTreeNode:
    """My custom node class used in binary trees."""

    def __init__(
            self,
            value=None
    ):
        """Initialize the node."""
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_value(
            self,
            value
    ):
        """Sets the value stored in the node."""
        self.value = value

    def get_value(
            self
    ):
        """Returns the value stored in the node."""
        return self.value

    def set_left_child(
            self,
            new_node
    ):
        """Sets the left child node."""
        self.left_child = new_node

    def get_left_child(
            self
    ):
        """Returns the left child node."""
        return self.left_child

    def set_right_child(
            self,
            new_node
    ):
        """Sets the right child node."""
        self.right_child = new_node

    def get_right_child(
            self
    ):
        """Returns the right child node."""
        return self.right_child


class MyBinaryTree:
    """My custom binary tree class."""

    def __init__(
            self
    ):
        """Initializes the binary tree."""
        self.root = None
        self.current_node = None

    def print_tree(
            self,
            top_node,
            tab_string=""
    ):
        """Prints the contents of the tree, where top_node is assumed to be the root."""
        position_of_node_in_tree = tab_string + str(top_node.get_value())
        left_child = top_node.get_left_child()
        right_child = top_node.get_right_child()

        print(position_of_node_in_tree)
        tab_string += "\t"

        if left_child is not None:
            self.print_tree(left_child, tab_string)

        if right_child is not None:
            self.print_tree(right_child, tab_string)

    def add(
            self,
            node_being_added_to,
            new_node,
            side
    ):
        """Adds new_node as a child node on the specified side (left or right)."""

        if self.root is None:
            self.root = new_node
        elif side == 'left':
            node_being_added_to.set_left_child(new_node)
        elif side == 'right':
            node_being_added_to.set_right_child(new_node)
