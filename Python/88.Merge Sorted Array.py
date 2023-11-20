
def merge(nums1, m, nums2, n):
    i = m-1 #last element of arr1
    j = n-1 #last element of arr2
    mn = (m+n) - 1 #last element of merged arr

    # loop over the merged array (arr1)
    while i>=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[mn] = nums1[i]
            i-=1
        else:
            nums1[mn] = nums2[j]
            j-=1
        mn-=1
    # merge the remaining elements in arr2 to arr1     
    while j >= 0:
        nums1[mn] = nums2[j]
        j -= 1
        mn -= 1

# Example 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

print("----------------------------------")

# Example 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

print("----------------------------------")

# Example 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]





