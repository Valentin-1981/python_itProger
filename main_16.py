nums1 = [5, 7, 3, 9, 4, 1, 4]
nums2 = [2.3, 4.5, 7.4, 6.9, 6.3]

min = nums1[0]
for el in nums1:
    if el < min:
        min = el

print(min)

def minimal(li):
    min_number = li[0]
    for el in li:
        if el < min_number:
            min_number = el
    return min_number

min1 = minimal(nums1)
min2 = minimal(nums2)

if min1 > min2:
    print(min2)
else:
    print(min1)

func = lambda x, y: x * y
res = func(5, 2)
print(res)
