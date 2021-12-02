from typing import Dict, List


def main() -> None:
    with open("input.txt") as input_file:
        directions: List[Dict]
        directions = [ {"command": i.split()[0], "amount": int(i.split()[1]) } for i in input_file.readlines()]
    
    x, y = 0, 0
    for direction in directions:
        command = direction["command"]
        amount = direction["amount"]
        if command == "forward":
            x += amount
        elif command == "up":
            y -= amount
        elif command == "down":
            y += amount
    
    print(x*y)
if __name__ == "__main__":
    main()