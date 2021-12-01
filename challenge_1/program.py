nums = [int(i) for i in open("nums.txt").read().splitlines()]
part_1 = sum(nums[i] > nums[i-1] for i in range(1,len(nums)))
part_2 = sum(sum(nums[i-3:i]) > sum(nums[i-4:i-1]) for i in range(4,len(nums)+1))
print(part_1)
print(part_2)

