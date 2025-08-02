# Ask the user for N
N = int(input("Enter a positive integer N: "))

# Read N numbers one by one into a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask for number X to search
X = int(input("Enter the number to search for (X): "))

# Search for X in the list
if X in numbers:
    # Find index (1-based)
    index = numbers.index(X) + 1
    print(index)
else:
    print(-1)
