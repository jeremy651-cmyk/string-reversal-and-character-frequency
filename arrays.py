numbers = [5, 15, 25, 35, 45]
print("Initial values:", numbers)

# Accessing an element from the list
print("Access element from the list")
position = int(input("Enter position to display: "))

# First direct access using index
if 0 <= position < len(numbers):
    print("Element found:", numbers[position])
else:
    print("Invalid index")

# Inserting a new element into the list
print("array insertion")
value = int(input("Enter value to insert: "))
place = int(input("Enter position to insert at: "))

# Insert element by creating a new list
if 0 <= place <= len(numbers):
    new_list = []
    for i in range(len(numbers) + 1):
        if i == place:
            new_list.append(value)
        if i < len(numbers):
            new_list.append(numbers[i])
    print("List after insertion:", new_list)
else:
    print("Invalid position")

# Deleting elements from the list
print("array deletion")

# Remove the last element
last_item = numbers[-1]
numbers = numbers[:-1]
print("Removed last element:", last_item)
print("List now:", numbers)