class MinHeap:
    def __init__(self):  # fixed here
        self.heap = [0]  # dummy zero to simplify index math
        self.size = 0

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

# Create heap object
h = MinHeap()

# List of elements to insert
t = [30, 25, 24, 23, 16, 15, 13, 12, 7, 5, 4, 3]

# Insert elements into heap
for i in t:
    h.insert(i)

# Print the heap (excluding dummy 0)
print("Min Heap:", h.heap[1:])

# Min Heap: [3, 5, 4, 13, 7, 15, 16, 30, 23, 24, 12, 25]