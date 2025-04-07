nums1 = [1, 2, 3, 0, 0, 0]
m = 0
nums2 = [2, 5, 6]
n = 1


temp1L = []
temp2R = nums2
for i in nums1:
    if i > 0 and i < m:
        temp1L.append(i)
    elif i == n or i == m:
        temp2R.append(i)
        temp2R.sort()


print(f"nums1:{temp1L}, nums2:{temp2R}")
# print(f"nums1:{temp1L[0]}, nums2:{temp2R[1]}")
