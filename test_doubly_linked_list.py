# Test MyDoublyLinkedList and MyDoubleNode

from my_doubly_linked_list import MyDoublyLinkedList

list = MyDoublyLinkedList()
list.add(10)
list.add(11)
list.add(12)
list.add(13)
list.add(14)
list.add(15)
list.add(10)
list.insert(10, 4)
list.print_list()
print()

list.delete_all_occurrences_of_value(10)

print()
list.print_list()