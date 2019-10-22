import copy
import operator
import math


class Median:
    def __init__(self):
        self.max_elements = []
        self.min_elements = []

    def __repr__(self):
        return "MAX:{}, MIN:{}".format(self.max_elements,
                                       self.min_elements)

    def __str__(self):
        return self.__repr__()

    def add_element(self, element):
        try:
            if element < self.max_elements[0]:
                self.min_elements.append(element)
                self.build_heapify()
            else:
                self.max_elements.append(element)
                self.build_inv_heapify()
        except IndexError:
            self.max_elements.append(element)

        if abs(len(self.min_elements) - len(self.max_elements)) > 1:
            if len(self.max_elements) > len(self.min_elements):
                self.min_elements.append(self.max_elements.pop(0))
            else:
                self.max_elements.append(self.min_elements.pop(0))
        self.build_heapify()
        self.build_inv_heapify()

    def get_median(self):
        if not self.min_elements:
            return self.max_elements[0]
        if not self.max_elements:
            return self.min_elements[0]
        if len(self.max_elements) > len(self.min_elements):
            return self.max_elements[0]
        elif len(self.max_elements) < len(self.min_elements):
            return self.min_elements[0]
        else:
            return self.min_elements[0], self.max_elements[0]

    def get_maxheap_elements(self):
        return self.min_elements

    def get_minheap_elements(self):
        return self.max_elements

    def build_heapify(self):
        for index in range(len(self.min_elements) // 2 + 1, -1, -1):
            self.heapify(index)

    def build_inv_heapify(self):
        for index in range(len(self.max_elements) // 2 + 1, -1, - 1):
            self.inv_heapify(index)

    def heapify(self, x=0):
        arr = self.min_elements
        left, right = 2 * x + 1, 2 * x + 2
        largest = left if (
                left <= len(self.min_elements) - 1
                and arr[left] > arr[x]) else x
        largest = right if (
                right <= len(self.min_elements) - 1
                and arr[right] > arr[largest]) else largest
        if largest != x:
            arr[x], arr[largest] = arr[largest], arr[x]
            self.min_elements = arr
            self.heapify(largest)

    def inv_heapify(self, x=0):
        arr = self.max_elements
        left, right = 2 * x + 1, 2 * x + 2
        smallest = left if (
                left <= len(self.max_elements) - 1
                and arr[left] < arr[x]) else x
        smallest = right if (
                right <= len(self.max_elements) - 1
                and arr[right] < arr[smallest]) else smallest
        if smallest != x:
            arr[x], arr[smallest] = arr[smallest], arr[x]
            self.max_elements = arr
            self.inv_heapify(smallest)


class Heap:
    def __init__(self, value, children=None):
        if children is None:
            children = []
        self.value = value
        self.children = children

    def __repr__(self):
        return "::{}::val {}: -> arr {}".format(self.__class__.__name__,
                                                self.value,
                                                [i for i in
                                                 self.children])

    def merge(self, other, comparator):
        first = copy.copy(self)
        if not other:
            pass
        elif comparator(first.value, other.value):
            new_list = first.children.copy()
            new_list.append(other)
            self.children = new_list
        else:
            new_list = other.children.copy()
            new_list.append(first)
            self.value = other.value
            self.children = new_list

    def insert(self, value):
        return self.merge(self.__class__(value))


class PairHeapMin(Heap):
    def __init__(self, value, children=None):
        if children is None:
            children = []
        super().__init__(value, children)

    def find_min(self):
        return self.value

    def merge(self, other, **kwargs):
        super().merge(other, operator.le)

    def delete_min(self):
        tmp = self.merge_pairs(self.children)
        self.value = tmp.value
        self.children = tmp.children

    @staticmethod
    def merge_pairs(l):
        if len(l) == 1:
            return l[0]
        elif len(l) == 2:
            l[0].merge(l[1])
            return PairHeapMin(l[0].value, l[0].children)
        else:
            l[0].merge(l[1])
            l[0].merge(PairHeapMin.merge_pairs(l[2:]))
            return PairHeapMin(l[0].value, l[0].children)


class PairHeapMax(Heap):
    def __init__(self, value, children=None):
        if children is None:
            children = []
        super().__init__(value, children)

    def find_max(self):
        return self.value

    def merge(self, other, **kwargs):
        super().merge(other, operator.ge)

    def delete_max(self):
        tmp = self.merge_pairs(self.children)
        self.value = tmp.value
        self.children = tmp.children

    @staticmethod
    def merge_pairs(l):
        if len(l) == 1:
            return l[0]
        elif len(l) == 2:
            l[0].merge(l[1])
            return PairHeapMax(l[0].value, l[0].children)
        else:
            l[0].merge(l[1])
            l[0].merge(PairHeapMax.merge_pairs(l[2:]))
            return PairHeapMax(l[0].value, l[0].children)


class PairingMedian:
    def __init__(self):
        self.len_min = 0
        self.len_max = 0
        self.heap_min = None
        self.heap_max = None

    def __str__(self):
        return "{}".format(self.get_median())

    def add_element(self, value):
        # for empty structure
        if self.len_min + self.len_max < 2:
            if not self.heap_max:
                self.heap_max = PairHeapMax(value)
                self.len_max += 1
            elif self.heap_max.find_max() > value:
                self.heap_min = PairHeapMin(self.heap_max.value)
                self.heap_max = PairHeapMax(value)
                self.len_min += 1
            else:
                self.heap_min = PairHeapMin(value)
                self.len_min += 1
        # for NON empty structure
        elif value < self.heap_max.value:
            self.heap_max.insert(value)
            self.len_max += 1
        else:
            self.heap_min.insert(value)
            self.len_min += 1
        if abs(self.len_min - self.len_max) > 1:
            if self.len_min > self.len_max:
                # self.heap_max.insert(PairHeapMax(self.heap_min.value))
                self.heap_max.insert(self.heap_min.value)
                self.heap_min.delete_min()
                self.len_min -= 1
                self.len_max += 1
            else:
                self.heap_min.insert(self.heap_max.value)
                # self.heap_min.insert(PairHeapMin(self.heap_max.value))
                self.heap_max.delete_max()
                self.len_min += 1
                self.len_max -= 1

    def get_median(self):
        if not self.heap_min:
            return self.heap_max.find_max()
        if not self.heap_max:
            return self.heap_min.find_min()

        if not (self.len_max + self.len_min) % 2:
            return self.heap_max.find_max(), self.heap_min.find_min()
        if self.len_max > self.len_min:
            return self.heap_max.find_max()
        return self.heap_min.find_min()


f = PairingMedian()
for i in range(10, 1, -1):
    f.add_element(i)
    print('i--------------->:', i)
    print(f.heap_min)
    print(f.heap_max)
    print(f.get_median())
#
# f = PairHeapMax(3)
# f.insert(4)
# f.insert(5)
# print(f)
# c = PairHeapMax(2)
# c.insert(10)
# c.insert(3)
# print(c)
# c.merge(f)
# print(c)
# c.delete_max()
# print(c)
