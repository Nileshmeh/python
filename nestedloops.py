rows = int(input("Enter the number of rows: "))
coloums = int(input("Enter the number of coloums: "))
symbols = input("Enter the symbol you want to use: ")

for x in range(rows):
    for y in range(coloums):
        print(symbols, end="")

    print()