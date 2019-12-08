# Given two strings A and B of lowercase letters,
# return true if and only if we can swap two letters in A so that the result equals B.


def buddy_strings(a, b):
    list_of_b = list(b)

    for i in range(0, len(a) - 1):

        for j in range(i+1, len(a)):
            list_of_a = list(a)

            temp = list_of_a[i]             # swap 2 letters in A ---> check whether equal to B
            list_of_a[i] = list_of_a[j]
            list_of_a[j] = temp

            if list_of_a == list_of_b:
                return True
    return False


a = input("Enter the string A : ") # Input 2 strings A & B
b = input("Enter the string B: ")
print(buddy_strings(a, b))
