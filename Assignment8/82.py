class MinHeap:
    def __init__(self):  # ✅ Fixed constructor
        self.heap = [0]  # dummy zero to make 1-based indexing easier
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

    def delete(self, value):
        # Find index of value
        if value not in self.heap:
            print(f"Value {value} not found in heap.")
            return
        index = self.heap.index(value)
        # Swap with last element
        self.heap[index], self.heap[self.size] = self.heap[self.size], self.heap[index]
        # Remove the last element
        self.heap.pop()
        self.size -= 1
        # Restore heap
        if index <= self.size:
            self.arrange(index)
            self.heapify_down(index)

# Testing Q2
h = MinHeap()
t = [30, 25, 24, 23, 16, 15, 13, 12, 7, 5, 4, 3]
for i in t:
    h.insert(i)

print("Heap before deletion:", h.heap[1:])
h.delete(7)
print("Heap after deleting 7:", h.heap[1:])


# Heap before deletion: [3, 5, 4, 13, 7, 15, 16, 30, 23, 24, 12, 25]
# Heap after deleting 7: [3, 5, 4, 13, 12, 15, 16, 30, 23, 24, 25]