# Input hashmap
data = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}

# Sorting by value
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

# Output
print(sorted_data)
