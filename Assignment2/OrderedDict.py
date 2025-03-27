from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict({
    'banana': 3,
    'apple': 5,
    'cherry': 2,
    'mango': 4
})

# Sort by keys
sorted_keys = OrderedDict(sorted(od.items()))
print("Sorted by keys:", sorted_keys)

# Sort by values
def get_value(item):
    return item[1]

sorted_values = OrderedDict(sorted(od.items(), key=get_value))
print("Sorted by values:", sorted_values)

# Sorted by keys: OrderedDict({'apple': 5, 'banana': 3, 'cherry': 2, 'mango': 4})
# Sorted by values: OrderedDict({'cherry': 2, 'banana': 3, 'mango': 4, 'apple': 5})
