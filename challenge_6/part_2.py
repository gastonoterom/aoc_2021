from collections import deque

def main() -> None:
    with open("input_test.txt") as i_f:
        numbers_str = i_f.read().strip().split(",")
        numbers = list(map(lambda n: int(n), numbers_str))

    bins = deque([numbers.count(i) for i in range(9)])

    print(bins)
    for i in range(256):
        bins[7] += bins[0]
        bins.rotate(-1)
        print(bins)
        
    print("Total fish:", sum(bins))            


if __name__ == "__main__":
    main()