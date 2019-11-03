import math
import random


class HashTable:
    def __init__(self, hash_type, values):
        if hash_type == 1:
            self.hashed = ChainDiv(values)
        elif hash_type == 2:
            self.hashed = ChainMul(values)
        else:
            pass
        self.values = values

    def __str__(self):
        return self.hashed.__str__()

    def get_collision_amount(self):
        return self.hashed.number_of_collisions

    def find_sum(self):
        pass


class Node:
    def __init__(self, item, next=None):
        """
        Produces a newly constructed is_empty node.
        __init__: Any -> Node
        Fields: item stores any value
        next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __repr__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return "{}".format(self.item)

    def __str__(self):
        return self.__repr__()


class LinkedList:
    """
    My Linked List from lab12 second semester first year
    """

    def __init__(self):
        """
        Produces a newly constructed is_empty LinkedList.
        __init__: -> LinkedList
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def __str__(self) -> str:
        current = self._head
        res = ''
        while current is not None:
            res += str(current.item) + '<=='
            current = current.next
        return res + "\n"

    def is_empty(self) -> bool:
        """
        Checks emptiness of list.
        is_empty: LinkedList -> Bool
        :return: True if LinkedList is is_empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the LinkedList.
        __contains__: LinkedList Any -> Bool
        :param value: the value to be check.
        :return: True if LinkedList is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.
        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            tmp = self._head
            self._head = Node(value)
            self._head.next = tmp

    def __sizeof__(self) -> int:
        """
        Return the size of LinkedList
        :return: the size of list
        """
        tmp = self._head
        counter = 0
        while tmp is not None:
            counter += 1
            tmp = tmp.next
        return counter


class ChainedHashTable:
    size: int
    elements: list

    def __init__(self, elements):
        self.elements = elements
        self.size = 3 * len(elements)
        self.table = [None] * self.size
        self.number_of_collisions = 0
        for each in elements:
            self.insert(each)

    def __str__(self):
        # return str(self.table)
        res = ""
        for each in self.table:
            if each is None:
                res += 'N\n'
            else:
                res += " --> {}".format(each)
        return res

    def insert(self, element):
        pass

    def delete(self, element):
        pass

    def search(self, element):
        pass

    def number_of_collisions(self):
        pass


class ChainDiv(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def insert(self, element):
        hash_value: int = element % self.size
        if self.table[hash_value] is None:
            self.table[hash_value] = LinkedList()
        else:
            self.number_of_collisions += 1
        self.table[hash_value].add(element)

    def delete(self, element):
        super().delete(element)

    def search(self, element):
        super().search(element)

    def number_of_collisions(self):
        pass


class ChainMul(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def insert(self, element):
        pass

    def delete(self, element):
        pass

    def search(self, element):
        pass


if __name__ == "__main__":
    # new = HashTable(1, [random.randint(1, 100) for i in range(10)])
    new = HashTable(1, [11, 21, 31, 41, 51, 61, 71, 81, 1, 2])
    print(new)
