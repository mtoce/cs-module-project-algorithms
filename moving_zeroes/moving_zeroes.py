'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0       # count of non-zero elements

    # Strategy: grab all non-zero elements and overwrite the beginning
    # elements up to the count of non-zero elements.
    # Then, overwrite the elements from the end of the count -> the end of the array
    # with zeroes

    # traverse array, if elem is non-zero replace elem at index 'count' with elem
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # once the non-zero elements have overwritten the past elements,
    # we can overwrite the elements from count -> end of array with zeroes
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")