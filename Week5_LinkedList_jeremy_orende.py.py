# Week 5 Assignment - Linked List
# Name: Jeremy Orende


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # checks if the list has anything
    def is_empty(self):
        return self.head is None

    # adds item to front
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # adds item to end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # shows the whole list
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # puts value somewhere in the list
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Wrong position")
            return

        new_node.next = current.next
        current.next = new_node

    # removes value from list
    def delete_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

        print("Not found")

    # finds where value is
    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index

            current = current.next
            index += 1

        return -1

    # counts items in list
    def size(self):
        total = 0
        current = self.head

        while current:
            total += 1
            current = current.next

        return total


if __name__ == "__main__":

    my_list = LinkedList()

    my_list.append(5)
    my_list.append(6)
    my_list.append(7)
    my_list.append(8)

    print("My starting list:")
    my_list.print_list()

    my_list.prepend(4)
    print("After adding 4 in front:")
    my_list.print_list()

    my_list.insert_at_position(9, 2)
    print("After adding 9:")
    my_list.print_list()

    my_list.delete_by_value(7)
    print("After removing 7:")
    my_list.print_list()

    print("Where is 9:", my_list.search(9))
    print("How many items:", my_list.size())
    print("is it Empty? ", my_list.is_empty())