***
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
***
program1:
elements = list(map(int, input().strip().split()))
reversed_elements = elements[::-1]
print(' '.join(map(str, reversed_elements)))
program2:
elements = list(map(int, input().strip().split()))
sorted_elements = sorted(elements)
print(' '.join(map(str, sorted_elements)))
