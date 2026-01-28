student_list=["Alice", "Bob", "Charlie", "David"]
student_tuple=("Alice", "Bob", "Charlie", "David")

## List Operations

print("Original List:", student_list)

# Add Elements:\
student_list.append("Alice")
student_list.append("Eve")
print("After Adding Elements:", student_list)

# Remove Elements:
student_list.remove("Bob")
print("After Removing Elements:", student_list)

# sort Elements:
student_list.sort()
print("After Sorting Elements in Ascending order:", student_list)

student_list.sort(reverse=True)
print("After Sorting Elements in Descending order:", student_list)

## Converting to list to set removing duplicate elements:
student_set=set(student_list)
print("After Converting to Set (removing duplicates):", student_set)

## Perform set operations:
set_B={"Charlie", "David", "Frank", "Grace"}

# Union
union_set=student_set.union(set_B)    
print("Union of Sets:", union_set)

# Intersection
intersection_set=student_set.intersection(set_B)
print("Intersection of Sets:", intersection_set)

# Difference
difference_set=student_set.difference(set_B)
print("Difference of Sets (student_set - set_B):", difference_set)
# Symmetric Difference
symmetric_difference_set=student_set.symmetric_difference(set_B)
print("Symmetric Difference of Sets:", symmetric_difference_set)

## Iterate through the collection:
print("Iterating through the student list:")
for student in student_list:
    print(student)

print("Iterating through the student tuple:")
for student in student_tuple:
    print(student)

print("Iterating through the student set:")
for student in student_set:
    print(student)

## With index (any iterable):
print("Iterating through the student list with index:")
for index, student in enumerate(student_list):
    print(f"Index {index}: {student}")

print("Iterating through the student tuple with index:")
for index, student in enumerate(student_tuple):
    print(f"Index {index}: {student}")

print("Iterating through the student set with index:")
for index, student in enumerate(student_set):
    print(f"Index {index}: {student}")

    
