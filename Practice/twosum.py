# Two  pointers approach to find if there are two numbers in the array that add up to the target
def twoSum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]

        # Check if the sum matches the target
        if sum == target:
            return True
        elif sum < target:
            
            # Move left pointer to the right
            left += 1
        else:
            
            # Move right pointer to the left
            right -= 1

    # If no pair is found
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    if twoSum(arr, target):
        print("true")
    else:
        print("false")



# Hashing approach to find if there are two numbers in the array that add up to the target
def twoSum(arr, target):
  
    # Create a set to store the elements
    s = set()

    for num in arr:
      
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    if twoSum(arr, target):
        print("true")
    else:
        print("false")