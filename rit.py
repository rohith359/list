***
Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
***
size = int(input().strip())
numbers = []

for _ in range(size):
    number = int(input().strip())
    numbers.append(number)

print(min(numbers))
