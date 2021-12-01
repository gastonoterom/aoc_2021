input=[int(l) for l in open("nums.txt").read().splitlines()]

part_1 = sum(b>a for a,b in zip(input[:len(input)-1], input[1:]))
part_2 = sum(b>a for a,b in zip(input[:len(input)-3], input[3:]))

print(part_1)
print(part_2)

