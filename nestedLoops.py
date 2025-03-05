rows = int(input("Type the number of rows:"))
columns = int(input("Type the number of columns:"))
symbol = input("Select a Symbol:")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()



