# Initialize an empty list
my_list = []

# Read the number of commands
n = int(input())

# Process each command
for _ in range(n):
    command = input().split()  # Read the command and split it into parts

    if command[0] == "insert":
        i, e = map(int, command[1:])  # Extract the index and element
        my_list.insert(i, e)
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        e = int(command[1])  # Extract the element to remove
        my_list.remove(e)
    elif command[0] == "append":
        e = int(command[1])  # Extract the element to append
        my_list.append(e)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()
