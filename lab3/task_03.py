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
        if len(self.max_elements) > len(self.min_elements):
            return self.max_elements[0]
        elif len(self.max_elements) < len(self.min_elements):
            return self.min_elements[0]
        else:
            return self.min_elements[0], self.max_elements[0]

    def get_max_heap_elements(self):
        return self.min_elements

    def get_min_heap_elements(self):
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


