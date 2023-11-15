# coding used in lecture of Wednesday, November 15
import random
import time

def bubble_sort(nums):
    """
    This function is an iterative implementation of the bubble
        sort algorithm.
    :param nums: a list of integers in random order
    :return: the list, sorted from smallest (element 0) to
        largest (element -1)
    """
    comparisons = 0
    swaps = 0
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            comparisons += 1
            if nums[j] > nums [j+1]: # 6 5
                swaps += 1
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    print("For Bubble sort:")
    print("comparisons: ", comparisons, " swaps: ", swaps)
    return nums

def selection_sort(nums):
    """
    This function is an iterative implementation of the
        selection sort algorithm
    :param nums: a list of integers in random order
    :return: the list, sorted from smallest (element 0) to
        largest (element -1)
    """
    comparisons = 0
    swaps = 0
    for i in range(len(nums)):

        # find the smallest element remaining in the
        # unsorted list. Start by presuming it's the
        # first element
        smallest = i
        for j in range(i + 1, len(nums)):
            comparisons += 1
            if nums[smallest] > nums[j]:
                smallest = j

        # When the loop is done, we know that smallest is
        # the index of the smallest value. Swap it
        # with the first element, unless the first element is
        #already the smallest
        if not (smallest == i):
            temp = nums[smallest]
            nums[smallest] = nums[i]
            nums[i] = temp
            swaps += 1
    print ("For Selection sort: ")
    print("comparisons: ", comparisons, " swaps: ", swaps)
    return nums

def quicksort(nums):
    """
    This function is a recursive implementation of the
        quicksort algorithm
    :param nums: a list of integers in random order
    :return: the list, sorted from smallest (element 0) to
        largest (element -1)

    """
    # base case - a list of length one is sorted
    global calls
    calls += 1
    if len(nums) <= 1:
        return nums
    # recursive case
    else:
        # pick a pivot - the first element
        pivot = nums[0]
        # define three empty lists, for elements greater than the pivot, less than the pivot, and equal to the pivot
        less = []
        equal = []
        greater = []
        # go through the list and put each element in the proper list
        for i in range(len(nums)):
            global comps
            comps += 1
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] == pivot:
               equal.append(nums[i])
            else:
               less.append(nums[i])

        results = quicksort(less) + equal + quicksort(greater)
        return(results)

def create_list_of_nums():
    list_of_nums = []
    size = int(input("How many numbers will be in the list?"))
    for i in range(size):
        list_of_nums.append(random.randint(1, 1000000))
    return list_of_nums

if __name__ == "__main__":
    list_of_nums = create_list_of_nums()
# lists are mutable. Once I sort the list, it is sorted
# and I cannot run the other algorithms on the same list to
# to get a fair comparison.
# so I will create 3 copies of the same list
    list2 = []
    list3 = []
    for i in range(len(list_of_nums)):
        list2.append(list_of_nums[i])
        list3.append(list_of_nums[i])

# call bubble sort on that list; see how many comparisons
# how many swaps and how much time it took
    bubble_start = time.time()
    first_list = bubble_sort(list_of_nums)
    bubble_end = time.time()
#    print(first_list)

# call selection sort on an identical list; see how
# many comparisons, how many swaps and how much time it took

    selection_start = time.time()
    second_list = selection_sort(list2)
    selection_end = time.time()
#    print(second_list)

# Call quicksort on a different copy of the list.
# Count how many recursive function calls were required,
# in addition to how much time and how many comparisons.
# There are no real swaps in quicksort.

# Note: we'll "cheat" and use two global variables in this
# function. It seems to be easier to explain how we're
# counting. In real life I'd pass these as arguments.

    calls = 0
    comps = 0
    quicksort_start = time.time()
    third_list = quicksort(list3)
    quicksort_end = time.time()
#    print(third_list)
    print("Quicksort took ", calls, " recursive function calls and ", comps, " comparisons")



    print("Now for time performances: ")
    print("Times given in seconds")
    print("Bubblesort took: ", bubble_end-bubble_start)
    print("Selection sort took: ", selection_end - selection_start)
    print("Quicksort took: ", quicksort_end - quicksort_start)
