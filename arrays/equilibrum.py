def equilibrum(self, arr):
    for i in range(0, len(arr)):
        leftSum = sum(arr[:i])
        rightSum = sum(arr[i+1:])
        if leftSum == rightSum:
            return i
        return -1


def equilibriumPoint(arr):
    prefSum = 0
    total = sum(arr)

    # Iterate pivot over all the elements
    # of the array and till prefSum != suffSum
    for pivot in range(len(arr)):
        suffSum = total - prefSum - arr[pivot]
        if prefSum == suffSum:
            return pivot
        prefSum += arr[pivot]

    return -1

if __name__ == "__main__":
    arr = [1, 7, 3, 6, 5, 6]

    result = equilibriumPoint(arr)
    print(result)