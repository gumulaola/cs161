nums = [7, 6, 4, 5, 3, 1, 2, 9, 8]


def insertSort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums


print(insertSort(nums))
