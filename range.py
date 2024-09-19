***
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
***
size = int(input().strip())
numbers = []

for _ in range(size):
    number = int(input().strip())
    numbers.append(number)

even_list = [num for num in numbers if num % 2 == 0]
odd_list = [num for num in numbers if num % 2 != 0]

print(f"The even list {even_list}")
print(f"The odd list {odd_list}")
