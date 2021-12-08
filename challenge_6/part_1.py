def main() -> None:
    with open("input_test.txt") as i_f:
        numbers_str = i_f.read().strip().split(",")
        numbers = list(map(lambda n: int(n), numbers_str))

    days = 32
    for _ in range(1, days+1):

        new_babies = 0
        for i, num in enumerate(numbers):
            
            if num == 0:
                new_babies += 1
                numbers[i] = 6
            else:
                numbers[i] -= 1

        for _ in range(new_babies):
            numbers.append(8)
        
    print("Total fish:", len(numbers))            


if __name__ == "__main__":
    main()