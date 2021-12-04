nums = [7, 6, 0, 5, 3, 1, 2, 9, 8]
k = 4


def select(nums, k):
    p = getPivot(nums)
    left, right, pivot = partition(nums, p)
    if k == len(left) + 1:
        return pivot
    elif k < len(left) + 1:
        return select(left, k)
    else:
        return select(right, k-len(left)-1)


# need to be improved: getPivot


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


print(select(nums, k))
