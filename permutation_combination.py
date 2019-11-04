def factorial_of_a_number(n):
    if n == 1:
        return 1
    else:
        return n*factorial_of_a_number(n-1)


def permutation(n, r):
    return factorial_of_a_number(n)//factorial_of_a_number(n-r)


def combination(n, r):
    return permutation(n, r)//factorial_of_a_number(r)


n = int(input("Enter the n value :"))
r = int(input("Enter the r value :"))
print(permutation(n, r))
print(combination(n, r))