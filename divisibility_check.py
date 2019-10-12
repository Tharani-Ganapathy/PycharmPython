def divisibilty(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("BOOYAKA")
        elif i % 3 == 0:
            print("BOO")
        elif i % 5 == 0:
            print("YAKA")


n = int(input("Enter the range : "))
divisibilty(n)