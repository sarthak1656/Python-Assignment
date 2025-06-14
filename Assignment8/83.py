class MinHeap:
    def __init__(self):  # ✅ Corrected constructor
        self.heap = [0]  # Dummy to make indexing start from 1
        self.size = 0

    def arrange(self, k):
        # Heapify up
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def heapify_down(self, k):
        # Heapify down
        while 2 * k <= self.size:
            min_child = self.get_min_child(k)
            if self.heap[k] > self.heap[min_child]:
                self.heap[k], self.heap[min_child] = self.heap[min_child], self.heap[k]
            k = min_child

    def get_min_child(self, k):
        if 2 * k + 1 > self.size:
            return 2 * k
        else:
            if self.heap[2 * k] < self.heap[2 * k + 1]:
                return 2 * k
            else:
                return 2 * k + 1

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def delete_min(self):
        if self.size == 0:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.heapify_down(1)
        return min_val

    def heap_sort(self):
        sorted_list = []
        while self.size > 0:
            sorted_list.append(self.delete_min())
        return sorted_list

# Testing Q3
t = [30, 25, 24, 23, 16, 15, 13, 12, 7, 5, 4, 3]
h = MinHeap()
for i in t:
    h.insert(i)

sorted_result = h.heap_sort()
print("Sorted list using heap sort:", sorted_result)


# Sorted list using heap sort: [3, 4, 5, 7, 12, 13, 15, 16, 23, 24, 25, 30]