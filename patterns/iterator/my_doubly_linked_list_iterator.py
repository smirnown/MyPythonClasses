"""This module contains my custom iterator for the MyDoublyLinkedList class."""

from  my_doubly_linked_list import MyDoublyLinkedList


class MyDoublyLinkedListIterator:
    """This is my attempt to code an iterator for python, making use of my_doubly_linked_list."""

    def __init__(
            self,
            linked_list=MyDoublyLinkedList
    ):
        """Initializes the iterator. Defaults to empty list if no linked list input."""
        self.node = linked_list.first_node

    def has_next(
            self
    ):
        """Returns True if there is a following node in the linked list. Else returns False."""
        if self.node.get_next_node():
            return True
        else:
            return False

    def has_previous(
            self
    ):
        """Returns True if there is a preceding node in the linked list. Else returns False."""
        if self.node.get_previous_node():
            return True
        else:
            return False

    def increment(
            self
    ):
        """Tells linked list to get next node. Doesn't return anything, though."""
        if self.has_next():
            self.node = self.node.get_next_node()

    def decrement(
            self
    ):
        """Tells linked list to get previous node. Doesn't return anything, though."""
        if self.has_previous():
            self.node = self.node.get_previous_node()

    def get_current_value(
            self
    ):
        """Returns the value of the node the linked list is currently looking at."""
        return self.node.value
