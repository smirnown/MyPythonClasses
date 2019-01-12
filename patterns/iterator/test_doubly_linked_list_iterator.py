# Test MyDoublyLinkedListIterator

from my_doubly_linked_list import MyDoublyLinkedList
from my_doubly_linked_list_iterator import MyDoublyLinkedListIterator

# Build a linked list
list = MyDoublyLinkedList()
i = 1

while i <= 100:
    list.add(i)
    i += 1


iterator = MyDoublyLinkedListIterator(list)
not_at_end_of_list = True

while not_at_end_of_list:
    print(iterator.get_current_value())

    if iterator.has_next():
        iterator.increment()
    else:
        not_at_end_of_list = False

print(iterator.node.get_next_node())

not_at_start_of_list = True
while not_at_start_of_list:
    print(iterator.get_current_value())

    if iterator.has_previous():
        iterator.decrement()
    else:
        not_at_start_of_list = False

print(iterator.node.get_previous_node())