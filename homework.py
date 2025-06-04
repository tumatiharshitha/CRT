
rows=int(input("Enter the number of the rows:"))
for i in range(1,rows+1):
    print("*"*i,end=" ")
    print(" "*(2*(rows-i)),end="")
    print("*"*i)
for i in range(rows,0,-1):
    print("*"*i,end=" ")
    print(" "*(2*(rows-i)),end=" ")
    print("*"*i)



n = 4
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))



n = 6
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


def zero_one_triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
zero_one_triangle(5)


def floyds_triangle(rows):
    number = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()
rows = int(input("Enter the number of rows: "))
floyds_triangle(rows)

def solve(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()

n = 5
solve(n)

