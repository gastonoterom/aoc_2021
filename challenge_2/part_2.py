with open("input.txt") as input_file:
    directions = [ {"command": i.split()[0], "amount": int(i.split()[1]) } for i in input_file.readlines()]
    
x = y = aim = 0
for direction in directions:
    command = direction["command"]
    amount = direction["amount"]
    if command == "forward":
        x += amount
        y += aim*amount
    elif command == "up":
        aim -= amount
    elif command == "down":
        aim += amount
    
print(x*y)
