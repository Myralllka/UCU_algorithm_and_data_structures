import math


class HashTable:
    def __init__(self, hash_type, values):
        if hash_type == 1:
            self.hash_table = ChainDiv(values)
        elif hash_type == 2:
            self.hash_table = ChainMul(values)
        elif hash_type == 3:
            self.hash_table = OpenAddressLine(values)
        elif hash_type == 4:
            self.hash_table = OpenAddressSqr(values)
        else:
            self.hash_table = OpenAddressDoubleHashing(values)
        self.values = values

    def __str__(self):
        """
        return string representation of the table
        :return str
        """
        return self.hash_table.__str__()

    def get_collisions_amount(self):
        """
        return number of collisions in the hash table
        :return int: number of collisions
        """
        return self.hash_table.number_of_collisions

    def find_sum(self, summ):
        for element in self.values:
            if summ - element in self.hash_table:
                if (summ - element == element and
                        self.hash_table.contains_twice(element)):
                    return element, element
                return summ - element, element
        return None


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

    def __str__(self):
        current = self._head
        res = ''
        while current is not None:
            res += str(current.item) + '<=='
            current = current.next
        return res + "\n"

    def is_empty(self):
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
        :return: True if value is in the LinkedList and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            current = current.next
        return False

    def contains_twice(self, value):
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

    def __sizeof__(self):
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

    def __contains__(self, item):
        """
        check if element is in hash table
        :param item: item to be searched
        :return boolean: True if element is in the table, False otherwise
        """
        hash_value = self.hash(item)
        if self.current_hash_table[hash_value] is not None and \
                item in self.current_hash_table[hash_value]:
            return True
        return False

    def __getitem__(self, item):
        hash_value = self.hash(item)
        return self.current_hash_table[hash_value].value

    def contains_twice(self, value):
        """
        check if the element is twice in the array
        :param value:
        :return:
        """
        hash_value = self.hash(value)
        if self.current_hash_table[hash_value] is not None and \
                self.current_hash_table[hash_value].contains_twice(value):
            return True
        return False

    def the_best_size(self):
        """
        abstract method to find the best size for the table
        """
        pass

    def insert(self, each):
        pass

    def hash(self, element):
        pass

    @staticmethod
    def factor(n):
        """
        method to find all divisors for the number
        :param n: number to be factored
        :return: list of divisors
        """
        return [i for i in range(1, n // 2 + 1) if n % i == 0]


class ChainDiv(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        return super().__contains__(item)

    def the_best_size(self):
        """
        the best divisor for this table is the prime number far away from
        powers of 2
        :return int: better size for the table
        """
        tmp = len(self.list_of_elements) // 2
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
        hash_value = self.hash(element)
        if self.current_hash_table[hash_value] is None:
            self.current_hash_table[hash_value] = LinkedList()
        else:
            self.number_of_collisions += 1
        self.current_hash_table[hash_value].add(element)

    def hash(self, element):
        return element % self.real_size_of_the_table


class ChainMul(ChainedHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        return super().__contains__(item)

    def the_best_size(self):
        return 2 ** round(math.log(len(self.list_of_elements), 2))

    def insert(self, element):
        hash_value = self.hash(element)
        if self.current_hash_table[hash_value] is None:
            self.current_hash_table[hash_value] = LinkedList()
        else:
            self.number_of_collisions += 1
        self.current_hash_table[hash_value].add(element)

    def hash(self, element):
        a = (math.sqrt(5) - 1) / 2
        return round(self.real_size_of_the_table * ((element * a) * 2 % 1)) - 1


class OpenAddressHashTable:
    def __init__(self, elements):
        """
        :param elements:
        """
        self.real_size_of_table = len(elements) * 3
        self.number_of_collisions = 0
        self.hash_table = [None] * self.real_size_of_table
        for each in elements:
            self.insert(each)

    def __str__(self):
        """
        :return:
        """
        result = ''
        for element in self.hash_table:
            result += '<<< ' + str(element) + '\n'
        return result[:-1]

    def __contains__(self, item):
        """
        :param item:
        :return:
        """
        i = 0
        j = self.hash(item, i)
        while self.hash_table[j] is not None and i < self.real_size_of_table \
                - 1:
            j = self.hash(item, i) % self.real_size_of_table
            if self.hash_table[j] == item:
                return True
            i += 1
        return False

    def contains_twice(self, item):
        """
        :param item:
        :return:
        """
        i = 0
        flag = False
        j = self.hash(item, i)
        while self.hash_table[j] is not None or i < self.real_size_of_table \
                - 1:
            j = self.hash(item, i) % self.real_size_of_table
            if self.hash_table[j] == item:
                if flag:
                    return True
                flag = True
            i += 1
        return False

    def hash(self, value, i):
        """
        return hashed value
        :param value: value to be hashed
        :param i: index
        :return: hashed number
        """
        pass

    def insert(self, item):
        """
        :param item:
        :return:
        """
        i = 0
        while i < self.real_size_of_table - 1:
            j = self.hash(item, i) % self.real_size_of_table
            if self.hash_table[j] is None:
                self.hash_table[j] = item
                return j
            else:
                i += 1
                self.number_of_collisions += 1
        print("error!!!")


class OpenAddressLine(OpenAddressHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        return super().__contains__(item)

    def insert(self, item):
        super().insert(item)

    def contains_twice(self, item):
        return super().contains_twice(item)

    def hash(self, value, i):
        return (value + i) % self.real_size_of_table - 1


class OpenAddressSqr(OpenAddressHashTable):
    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        return super().__contains__(item)

    def insert(self, item):
        super().insert(item)

    def contains_twice(self, item):
        return super().contains_twice(item)

    def hash(self, value, i):
        additional_hash = value % (self.real_size_of_table // 4) - 1
        return additional_hash + i + 6 * i ** 2


class OpenAddressDoubleHashing(OpenAddressHashTable):

    def __init__(self, elements):
        super().__init__(elements)

    def __contains__(self, item):
        return super().__contains__(item)

    def insert(self, item):
        return super().insert(item)

    def contains_twice(self, item):
        return super().contains_twice(item)

    def hash(self, value, i):
        additional_hash_one = value % (self.real_size_of_table // 4) - 1
        additional_hash_two = value % self.real_size_of_table - 1
        return (additional_hash_one +
                i * additional_hash_two) % self.real_size_of_table


if __name__ == "__main__":
    import random

    new2 = HashTable(5, [random.randint(1, 10000000000) for i in range(
            100000)])
    # new2 = HashTable(4, [11, 12, 14, 1, 15, 16, 12, 18, 19])
    print(new2)
    print(new2.find_sum(6000000000))
    print(new2.get_collision_amount())
