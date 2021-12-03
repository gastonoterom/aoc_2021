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

    positions = [i for i in range(len(codes))]
    candidate_codes = [codes[i] for i in positions]

    for pos in aux_array:
        if len(candidate_codes) == 1:
            break
        ones = 0
        zeros = 0
        for j, char_pos in enumerate(pos):
            if j not in positions:
                continue
            if char_pos == "1":
                ones += 1
            if char_pos == "0":
                zeros += 1
        
        i = 0
        for char in pos:
            if i not in positions:
                i+=1
                continue
            if ones>=zeros:
                if char == "0":
                    positions.remove(i)
            if zeros>ones:
                if char == "1":
                    positions.remove(i)
            i+=1

        candidate_codes = [codes[i] for i in positions]

    gamma = int(codes[positions[0]] ,2)

    positions = [i for i in range(len(codes))]
    candidate_codes = [codes[i] for i in positions]
    for pos in aux_array:
        if len(candidate_codes) == 1:
            break
        ones = 0
        zeros = 0
        for j, char_pos in enumerate(pos):
            if j not in positions:
                continue
            if char_pos == "1":
                ones += 1
            if char_pos == "0":
                zeros += 1
        
        i = 0
        for char in pos:
            if i not in positions:
                i+=1
                continue
            if ones<zeros:
                if char == "0":
                    positions.remove(i)
            if zeros<=ones:
                if char == "1":
                    positions.remove(i)
            i+=1

        candidate_codes = [codes[i] for i in positions]
    epsilon = int(codes[positions[0]] ,2)

    print(gamma * epsilon)

main()