nums = [7, 6, 0, 5, 3, 1, 2, 9, 8]


def quickSort(nums):
    if len(nums) <= 1:
        return nums
    p = getPivot(nums)
    left, right, pivot = partition(nums, p)
    left = quickSort(left)
    right = quickSort(right)
    left = list(left)
    right = list(right)
    left.append(pivot)
    left.extend(right)
    return left


def getPivot(nums):
    return round(len(nums)/2)


def partition(nums, p):
    pivot = nums[p]
    left = []
    right = []
    for i in range(len(nums)):
        if i == p:
            continue
        else:
            if nums[i] <= nums[p]:
                left.append(nums[i])
            else:
                right.append(nums[i])
    return left, right, pivot


print(quickSort(nums))
