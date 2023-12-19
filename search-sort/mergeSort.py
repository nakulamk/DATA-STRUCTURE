def ms(lb, ub, a):
    if lb < ub:
        mid = (lb + ub) // 2
        ms(lb, mid, a)
        ms(mid + 1, ub, a)
        merge(lb, mid, ub, a)


def merge(lb, mid, ub, a):
    i = lb
    j = mid + 1
    k = lb
    b = [0] * len(a)  # Initialize b with proper values

    while i <= mid and j <= ub:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1

    while j <= ub:
        b[k] = a[j]
        j += 1
        k += 1

    # Copy the sorted elements back to the original array 'a'
    for x in range(lb, ub + 1):
        a[x] = b[x]

# Example usage
a = [8, 1, 15, 5, 24]
lb = 0
ub = len(a) - 1
ms(lb, ub, a)

# Print the sorted array
print("Sorted Array:", a)




# Let's perform a dry run of the provided Merge Sort code step by step using the example array `[8, 1, 15, 5, 24]`. The goal is to illustrate how the array is split into smaller segments and then merged back together in a sorted manner.

# ### Initial State:

# - Original Array: `[8, 1, 15, 5, 24]`
# - lb (lower bound): 0
# - ub (upper bound): 4

# ### Initial Call to `ms(lb, ub, a)`:

# 1. **First Recursive Call:**
#    - `ms(0, 2, a)` (left half of the array)
#      - Split `[8, 1, 15]`
#      - `ms(0, 1, a)` (left half of the left half)
#        - Split `[8, 1]`
#        - `ms(0, 0, a)` (single element, no further split)
#        - `ms(1, 1, a)` (single element, no further split)
#        - Merge `[8]` and `[1]` into sorted `[1, 8]`
#      - `ms(2, 2, a)` (single element, no further split)
#      - Merge sorted `[1, 8]` and `[15]` into sorted `[1, 8, 15]`

# 2. **Second Recursive Call:**
#    - `ms(3, 4, a)` (right half of the array)
#      - Split `[5, 24]`
#      - `ms(3, 3, a)` (single element, no further split)
#      - `ms(4, 4, a)` (single element, no further split)
#      - Merge sorted `[5]` and `[24]` into sorted `[5, 24]`

# 3. **Final Merge:**
#    - Merge sorted `[1, 8, 15]` and `[5, 24]` into the final sorted array `[1, 5, 8, 15, 24]`

# ### Final Sorted Array:

# The final sorted array is `[1, 5, 8, 15, 24]`, which is the correct result of applying the Merge Sort algorithm to the initial array `[8, 1, 15, 5, 24]`.
