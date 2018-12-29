"""
This module contains my custom linked list classes:
Nodes, linked lists, doubly-linked lists, circular linked lists, and doubly-circular linked lists.
"""


class MyNode:
    """This is my attempt to code a node for use in linked lists."""

    # Instance variables
    value = 0
    next_node = None

    def __init__(
            self,
            value=0
    ):
        """Initialize the node."""
        self.value = value
        self.next_node = None

    def set_value(
            self,
            value
    ):
        """Set value of current node."""
        self.value = value

    def get_value(
            self
    ):
        """Return value of node."""
        return self.value

    def set_next_node(
            self,
            new_node
    ):
        """Set next node."""
        self.next_node = new_node

    def get_next_node(
            self
    ):
        """Move to next node."""
        return self.next_node


class MyLinkedList:
    """"This is my attempt to code a linked list."""

    first_node = None
    last_node = None

    def __init__(
            self,
    ):
        """Initialize the linked list."""
        self.first_node = None
        self.last_node = None

    def print_list(
            self
    ):
        """Prints the contents of the linked list."""
        current_node = self.first_node

        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_next_node()

    def add(
            self,
            value
    ):
        """Adds a new node to the end of the linked list."""
        new_node = MyNode(value)
        list_is_empty = self.first_node is None

        if list_is_empty:
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.last_node.set_next_node(new_node)
            self.last_node = new_node

    def size(
            self
    ):
        """Returns the size of the linked_list."""
        size = 0
        temp_node = self.first_node

        while temp_node is not None:
            size += 1
            temp_node = temp_node.get_next_node()
        return size

    def get_node(
            self,
            index
    ):
        """Returns the node at the specified index."""
        i = 0
        current_node = self.first_node

        while i < index:
            current_node = current_node.get_next_node()
            i += 1
        return current_node

    def get_value(
            self,
            index
    ):
        """Returns the value from the node at the given index."""
        value = self.get_node(index).get_value()
        return value

    def __insert_node_at_beginning(
            self,
            new_node
    ):
        """Inserts a new node at the beginning of a linked list."""
        new_node.set_next_node(self.first_node)
        self.first_node = new_node

    def __insert_node_in_middle(
            self,
            new_node,
            index
    ):
        """Inserts a new node anywhere after the beginning of a linked list."""
        node_before_inserted_node = self.get_node(index - 1)
        node_after_inserted_node = self.get_node(index)

        node_before_inserted_node.set_next_node(new_node)
        new_node.set_next_node(node_after_inserted_node)

    def __insert_node_at_end(
            self,
            new_node
    ):
        """Inserts a node at the end of a linked list and updates 'last_node'."""
        self.last_node.set_next_node(new_node)
        self.last_node = new_node

    def insert(
            self,
            value,
            index
    ):
        """Inserts a node containing 'value' at 'node_index'."""
        new_node = MyNode(value)
        size_of_list = self.size()
        inserting_node_at_start_of_list = index == 0
        inserting_node_in_middle_of_list = (index > 0) and (index < size_of_list)
        inserting_node_at_end_of_list = index == size_of_list

        if inserting_node_at_start_of_list:
            self.__insert_node_at_beginning(new_node)
        elif inserting_node_in_middle_of_list:
            self.__insert_node_in_middle(new_node, index)
        elif inserting_node_at_end_of_list:
            self.__insert_node_at_end(new_node)
        else:
            print("There is no node of index " + str(index))

    def exists(
            self,
            value
    ):
        """Checks if the specified value is stored anywhere in the linked list."""
        size_of_list = self.size()
        index = 0

        while index < size_of_list:
            if self.get_value(index) == value:
                return True
            index += 1
        return False

    def __delete_first_node(
            self
    ):
        """Deletes the first node in the linked list."""
        self.first_node = self.get_node(1)

    def __delete_node_in_middle(
            self,
            index
    ):
        """Deletes a node in the middle of the linked list."""
        node_after_deleted_node = self.get_node(index + 1)
        node_before_deleted_node = self.get_node(index - 1)
        node_before_deleted_node.set_next_node(node_after_deleted_node)

    def __delete_last_node(
            self
    ):
        """Deletes the last node in the linked list."""
        size_of_list = self.size()
        node_before_last_node = self.get_node(size_of_list - 2)
        node_before_last_node.set_next_node(None)
        self.last_node = node_before_last_node

    def delete_by_index(
            self,
            index
    ):
        """Removes the node at the specified index from the linked list."""
        last_index = self.size() - 1
        deleting_first_node = index == 0
        deleting_node_in_middle = (index > 0) and (index < last_index)
        deleting_last_node = index == last_index

        if deleting_first_node:
            self.__delete_first_node()
        elif deleting_node_in_middle:
            self.__delete_node_in_middle(index)
        elif deleting_last_node:
            self.__delete_last_node()
        else:
            print("There is no node of index " + str(index))

    def delete_first_occurrence_of_value(
            self,
            value_to_be_deleted
    ):
        """Deletes the first node with the specified value."""
        index = 0
        size_of_list = self.size()

        while index < size_of_list:
            current_value = self.get_value(index)

            if current_value == value_to_be_deleted:
                self.delete_by_index(index)
                break
            else:
                index += 1

    def delete_all_occurrences_of_value(
            self,
            value_to_be_deleted
    ):
        """Deletes all nodes with the specified value."""
        while self.exists(value_to_be_deleted):
                self.delete_first_occurrence_of_value(value_to_be_deleted)

