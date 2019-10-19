class Median:
    def __init__(self):
        self.max_elements = []
        self.min_elements = []
        self.number_of_elements = 0
        self.max_elements_number = 0
        self.min_elements_number = 0

    def __repr__(self):
        return "MAX:{}, MIN:{}".format(self.max_elements, self.min_elements)

    def __str__(self):
        return self.__repr__()

    def add_element(self):
        pass

    def get_median(self):
        pass

    def get_maxheap_elements(self):
        pass

    def get_minheap_elements(self):
        pass

    def nogrowing_rebalance(self):
        pass

    def nodeclining_rebalance(self):
        pass
