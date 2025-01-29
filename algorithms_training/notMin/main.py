def notMin(nums, start, finish):
    min = nums[start]
    for el in range(start, finish + 1):
        if nums[el] > min:
            return nums[el]
        elif nums[el] < min:
            return min
    return "NOT FOUND"


n, m = map(int, input().split())
nums = [int(x) for x in input().split()]
answers = []
for req in range(m):
    answers.append(notMin(nums, *map(int, input().split())))
for ans in answers:
    print(ans)