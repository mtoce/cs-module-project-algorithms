'''
Input: a List of integers
Returns: a List of integers
'''
import numpy as np

def product_of_all_other_numbers(arr):

    # Why is type(arr) a list? And why are we calling our input arr if it isnt an array?
    # print(type(arr))
    arr = np.array(arr)
    # print(type(arr))

    prod_arr = []
    
    # use list comp to create a new list to take the product of at counter i
    i = 0
    for i in range(len(arr)):
        #print(i)
        # we will use boolean indexing with numpy due to it's fast opperational time
        # boolean indexing didnt work because of duplicates - instead we use list comp and enumerate
        take_prod_of_this = [x for j, x in enumerate(arr) if j != i]
        print(take_prod_of_this)
        # now we utilize numpy.arr.prod to get the product of the array and
        # insert it at the current position i
        prod_arr.append(np.prod(take_prod_of_this))
        #print(prod_arr)
    print(prod_arr)
    return prod_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    expected = [13547520, 10536960, 94832640, 11854080, 15805440, 13547520, 11854080, 11854080, 13547520, 9483264]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    print(f"Expected Output of product_of_all_other_numbers: {expected}")
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
