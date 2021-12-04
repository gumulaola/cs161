nums = [7, 6, 4, 5, 3, 1, 2, 9, 8]


def merge(l, r):
    i = 0
    j = 0
    ret = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            ret.append(l[i])
            i += 1
        else:
            ret.append(r[j])
            j += 1
    while i < len(l):
        ret.append(l[i])
        i += 1
    while j < len(r):
        ret.append(r[j])
        j += 1
    return ret


def mergeSort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    l = mergeSort(nums[:round(n/2)])
    r = mergeSort(nums[round(n/2):n])
    return merge(l, r)


print(mergeSort(nums))
