def ternarySearch(arr, left, right, target):#array-list,left-starting index,right-ending index
    while left <= right:#the loop continues as long as left is less or equal to right
        # Ensure mid1 and mid2 are integers
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if the target is at mid1 or mid2
        if arr[mid1] == target:
            return mid1#mid 1 is the target value  if so it returns mid 1 as the target value
        if arr[mid2] == target:
            return mid2#checks if the element at mid2 is the target value is so it returns mid 2 as the target value

        # Narrow down the search space
        if target < arr[mid1]:
            right = mid1 - 1#if the target is smaller than the arr it can only be on the left side of the array so we update right to (mid1-1)
        elif target > arr[mid2]:
            left = mid2 + 1#if the target is greater than the arr it can only be in the rightmost part of the arrso we update left to (mid2+1)
        else:
            left = mid1 + 1
            right = mid2 - 1
#else if its between the two then it must be in the middle third

    return -1
    # Return -1 if the target is not found

# Main function to test ternarySearch
def main():
    # Sample sorted array
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]#list
    target = 7  # Element we want to search for

    # Perform ternary search
    result = ternarySearch(arr, 0, len(arr) - 1, target)#we call it ternary search target to search the target within the array 0 and len(arr)-1 to define the end of the array



    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in array.")

# Run main
if __name__ == "__main__":
    main()
