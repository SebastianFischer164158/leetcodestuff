from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    answer = []
    for number in nums:
        count1 = 0
        for j in nums:
            if j != number and j < number:
                count1 += 1
        answer.append(count1)
    return answer


nums1 = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums1))
nums2 = [6, 5, 4, 8]
print(smallerNumbersThanCurrent(nums2))
nums3 = [7, 7, 7, 7]
print(smallerNumbersThanCurrent(nums3))
