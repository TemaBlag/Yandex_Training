def binarySearch(nums, num, start, finish):
    if start == finish:
        if nums[start] == num:
            return num
        return nums[start] if num - nums[start - 1] > nums[start] - num else nums[start - 1]
    mid = (start + finish) // 2
    if nums[mid] > num:
        return binarySearch(nums, num, start, mid)
    if nums[mid] < num:
        return binarySearch(nums, num, mid + 1, finish)
    else:
        return num

n = int(input())
nums = list(map(int, input().split()))
mins = [0] * n
maxs = [sum(map(lambda x: abs(x - nums[0]), nums))] * n
print(maxs[0] + mins[0], end=" ")
for i in range(1, n):
    dif = nums[i] - nums[i-1]
    mins[i] = mins[i - 1] + (i+1)*dif
    maxs[i] = maxs[i-1] - (n-i+1)*dif
    print(maxs[i] + mins[i], end=" ")


