from statistics import mean
from math import floor, ceil

def get_fuel(locations, x) -> int:
    return sum( sum(i+1 for i in range(abs(x-l))) for l in locations )

def get_cheapest_fuel(locations) -> int:
    return min(get_fuel(locations,floor(mean(locations))), get_fuel(locations,ceil(mean(locations))))

def main() -> None:
    with open("input.txt") as input_f:
        numbers = [int(i) for i in input_f.read().rstrip().split(",")]
        
    print(get_cheapest_fuel(numbers))

if __name__ == "__main__":
    main()



