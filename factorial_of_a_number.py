def factorial_of_a_number(n):
    if n == 1:
        return 1
    else:
        return n*factorial_of_a_number(n-1)


n = int(input("Enter the number to find factorial :"))
print(factorial_of_a_number(n))