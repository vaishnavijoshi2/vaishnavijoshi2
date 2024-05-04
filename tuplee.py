# Read input
n = int(input())
int_list = [int(i) for i in input().split()]

# Create a tuple from the input list
int_tuple = tuple(int_list)

# Compute and print the hash value of the tuple
print(hash(int_tuple))
