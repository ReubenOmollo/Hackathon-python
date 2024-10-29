def find_kth_largest_sort(arr, k):#This line defines a function called find_kth_largest_sort that takes two parameters.
#array-list.
# k-represents an integer representing which largest element to find (1 for the largest, 2 for the second largest, etc.).

    # Sort the list in descending order
    arr.sort(reverse=True)
    #This line sorts the arr list in place using the sort() method with the reverse=True argument.
    #Sorting in descending order means the largest elements will come first in the list.
    #After this line, the original arr will be modified to contain its elements in descending order.

    return arr[k - 1]
    #This line returns the Kth largest element from the sorted list.

# Example usage
arr = [3, 2, 1, 5, 6, 4]
k = 6
print("Kth largest element:", find_kth_largest_sort(arr, k)) 
#This line calls the find_kth_largest_sort function, passing arr and k as arguments.
#The function returns the 2nd largest element, which is printed to the console.
