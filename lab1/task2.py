import time


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums) // 2]
        less = []
        more = []
        equals = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                equals.append(i)
        return quick_sort(less) + equals + quick_sort(more)


def bubble_sort(nums):
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    n = len(nums)
    swapped = True

    elem = -1
    while swapped:
        swapped = False
        elem += 1
        for i in range(1, n - elem):
            if nums[i - 1] > nums[i]:
                swap(i - 1, i)
                swapped = True
    return nums


t0 = time.perf_counter()
print(quick_sort([111, 435, 3, 23, 37, 5, 3, 111, 435, 3, 23, 37]))
print(time.perf_counter() - t0)
print(bubble_sort([111, 435, 3, 23, 37, 5, 3, 111, 435, 3, 23, 37]))
print(time.perf_counter() - t0)
