# Test MyLinkedListIterator

from my_linked_list import MyLinkedList
from my_linked_list_iterator import MyLinkedListIterator

# Build a linked list
list = MyLinkedList()
i = 1

while i <= 100:
    list.add(i)
    i += 1


iterator = MyLinkedListIterator(list)
not_at_end_of_list = True

while not_at_end_of_list:
    print(iterator.get_current_value())

    if iterator.has_next():
        iterator.increment()
    else:
        not_at_end_of_list = False
