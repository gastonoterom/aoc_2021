from statistics import median

def get_cheapest_location(locations):
    return median(locations)

def main() -> None:
    with open("input.txt") as input_f:
        numbers = [int(i) for i in input_f.read().rstrip().split(",")]

    desired_location = get_cheapest_location(numbers)
    fuel = 0
    for number in numbers:
        fuel += abs(number-desired_location)

    print(fuel)


if __name__ == "__main__":
    main()