import math
import random


class HashTable:
    def __init__(self, hash_type, values):
        if hash_type == 1:
            self.hash_table = ChainDiv(values)
        elif hash_type == 2:
            self.hash_table = ChainMul(values)
        else:
            pass
        self.values = values

    def __str__(self) -> str:
        """
        return string representation of the table
        :return str
        """
        return self.hash_table.__str__()

    def get_collision_amount(self) -> int:
        """
        return number of collisions in the hash table
        :return int: number of collisions
        """
        return self.hash_table.number_of_collisions

    def find_sum(self, sum):
        """

        :param sum:
        :return:
        """
        pass
        # if sum in self.hashed:
        #     return self.hashed[sum]


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

    def __repr__(self) -> str:
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return "{}".format(self.item)

    def __str__(self) -> str:
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

    def __contains__(self, value) -> bool:
        """
        Checks existence of value in the LinkedList.
        __contains__: LinkedList Any -> Bool
        :param value: the value to be check.
        :return: True if value is in the LinkedList and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            current = current.next
        return False

    def contains_twice(self, value) -> bool:
        """
        check if element is two times in the list
        :param value: value to be checked
        :return: True if contains, False otherwise
        """
        current = self._head
        flag = False
        while current is not None:
            if current.item == value and flag:
                return True
            elif current.item == value:
                flag = True
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
    real_size_of_the_table: int
    list_of_elements: list

    def __init__(self, elements):
        """
        initialisation of the general class for chain hash tables
        :param elements: list of elements to be added to the hash table
        """
        self.list_of_elements = elements
        self.real_size_of_the_table = self.the_best_size()
        self.current_hash_table = [None] * self.real_size_of_the_table
        self.number_of_collisions = 0
        for each in elements:
            self.insert(each)

    def __str__(self):
        result = ""
        for each in self.current_hash_table:
            if each is None:
                result += 'N\n'
            else:
                result += " --> {}".format(each)
        return result

    @staticmethod
    def factor(n):
        """
        method to find all divisors for the number
        :param n: number to be factored
        :return: list of divisors
        """
        return [i for i in range(1, n // 2 + 1) if n % i == 0]

    def contained_twice(self, value):
        """
        check if the element is twice in the array
        :param value:
        :return:
        """
        hash_value = value % self.real_size_of_the_table
        if self.current_hash_table[hash_value] is not None and \
                self.current_hash_table[hash_value].containes_twice(value):
            return True
        return False

    def the_best_size(self) -> int:
        """
        abstract method to find the best size for the table
        """
        pass

    def __contains__(self, item):
        """
        check if element is in hash table
        :param item: item to be searched
        :return boolean: True if element is in the table, False otherwise
        """
        hash_value = item % self.real_size_of_the_table
        if self.current_hash_table[hash_value] is not None and \
                item in self.current_hash_table[hash_value]:
            return True
        return False

    def insert(self, each):
        pass

    def __getitem__(self, item):
        hash_value = item % self.real_size_of_the_table

        return self.current_hash_table[hash_value].value


class ChainDiv(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        super().__contains__(item)

    def the_best_size(self) -> int:
        """
        the best divisor for this table is the prime number far away from
        powers of 2
        :return int: better size for the table
        """
        tmp: int = len(self.list_of_elements) // 2
        while tmp >= 3:
            if len(self.factor(tmp)) == 1:
                return tmp
            tmp -= 1
        return tmp

    def insert(self, element):
        """
        inserted the element to the hash table
        :param element: the element to be inserted
        """
        hash_value: int = element % self.real_size_of_the_table
        if self.current_hash_table[hash_value] is None:
            self.current_hash_table[hash_value] = LinkedList()
        else:
            self.number_of_collisions += 1
        self.current_hash_table[hash_value].add(element)


class ChainMul(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        super().__contains__(item)

    def the_best_size(self) -> int:
        return 2 ** round(math.log(len(self.list_of_elements), 2))

    def insert(self, element):
        a = (math.sqrt(5) - 1) / 2
        hash_value = round(
                self.real_size_of_the_table * ((element * a) * 2 % 1))
        if self.current_hash_table[hash_value] is None:
            self.current_hash_table[hash_value] = LinkedList()
        else:
            self.number_of_collisions += 1
        self.current_hash_table[hash_value].add(element)


if __name__ == "__main__":
    new = HashTable(1, [random.randint(1, 100) for i in range(50)])
    # new = HashTable(1, [11, 21, 31, 41, 51, 61, 71, 81, 1, 2])
    new2 = HashTable(2, [random.randint(1, 50000) for i in range(100000)])
    print(new2)
    print(new2.get_collision_amount())
    # print(new.hashed.factor(17))
