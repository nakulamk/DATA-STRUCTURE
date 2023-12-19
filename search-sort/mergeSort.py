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
