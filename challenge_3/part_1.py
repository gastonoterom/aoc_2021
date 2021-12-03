from typing import List
 
def main() -> None:
    with open("input.txt") as input_file:
        codes = [code.strip() for code in input_file.readlines()]

    aux_array: List[str] = [""] * 12
    for i in range(len(codes)):
        code = codes[i]
        j=0
        for letter in code:
            aux_array[j] += letter
            j+=1

    gamma = ""
    for chars in aux_array:
        ones = 0
        zeros = 0
        for char in chars:
            if char == "1":
                ones +=1
            else:
                zeros += 1
        if ones>zeros:
            gamma += "1"
        else:
            gamma += "0"
    epsilon = ""
    for char in gamma:
        if char == "1":
            epsilon += "0"
        else:
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))
main()