from typing import List


# list_of_subarray_lens = []
# for num in range(1, len_array + 1):
#    if num % 2 != 0:
#        list_of_subarray_lens.append(num)

def sumOddLengthSubarrays(arr: List[int]) -> int:
    len_array = len(arr)
    list_of_subarray_lens = [num for num in range(1, len_array + 1) if
                             num % 2 != 0]
    total_sum = 0

    for subarray_len in list_of_subarray_lens:
        for i in range(len(arr)):
            if subarray_len + i > len_array:
                break
            else:
                # print(f"START: {x} <-> END: {subarray_len - 1 + x}")
                subarray = arr[i:subarray_len + i]
                # print(subarray)
                subarray_sum = sum(subarray)
                # print("SUM -> ", subarray_sum)
                total_sum += subarray_sum
    return total_sum


y = sumOddLengthSubarrays([10, 11, 12])
print(y)
